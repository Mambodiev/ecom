
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core import paginator
from django.http.response import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.shortcuts import reverse, render
from django.views import generic
from django.views.generic.list import ListView
from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import TrigramSimilarity

from .models import Carousel, About, Faq, Shipping_returns, Terms_of_use, Privacy_policy
from cart.models import Order, Product
from django.http import HttpResponse, HttpResponseRedirect, request
from django.utils import translation
from django.utils.translation import gettext as _
from .forms import ContactForm, SearchForm


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.annotate(
                similarity=TrigramSimilarity('title', query),
            ).filter(similarity__gt=0.1).order_by('-similarity')
    return render(request,
                  'cart/product/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})



class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({
            "orders": Order.objects.filter(user=self.request.user, ordered=True)
        })
        return context


def home(request):

    product = Product.objects.all()
    carousel = Carousel.objects.all()

    paginator = Paginator(product, per_page=4)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    products_latest = Product.objects.all().order_by('id')[:4]
    products_picked = Product.objects.all().order_by('?')[:4]

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'page': 'page',
        'product': page_obj.object_list,
        'carousel': carousel,
        'paginator': paginator,
        'page_number': int(page_number),
        'products_latest':products_latest,
        'products_picked':products_picked,
    }

    return render(request, 'home.html',context)


# def selectlanguage(request):
#     if request.method == 'POST':  # check post
#         cur_language = translation.get_language()
#         lasturl = request.META.get('HTTP_REFERER')
#         lang = request.POST['language']
#         translation.activate(lang)
#         request.session[translation.LANGUAGE_SESSION_KEY] = lang
#         # return HttpResponse(lang)
#         return HttpResponseRedirect("/" + lang)

def change_language(request):
    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = f'/{language}/'
            elif language == settings.LANGUAGE_CODE:
                redirect_path = '/'
            else:
                return response
            from django.utils import translation
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response


class AboutListView(ListView):
    model = About
    template_name = 'about.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.all()
        return context
        
    
class FaqListView(ListView):
    model = Faq
    template_name = 'faq.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['faq'] = Faq.objects.all()
        return context


class Terms_of_useListView(ListView):
    model = Terms_of_use
    template_name = 'terms_of_use.html'
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['terms_of_use'] = Terms_of_use.objects.all()
        return context


class Privacy_policyListView(ListView):
    model = Privacy_policy
    template_name = 'privacy_policy.html'
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['privacy_policy'] = Privacy_policy.objects.all()
        return context


class Shipping_returnsListView(ListView):
    model = Shipping_returns
    template_name = 'shipping_returns.html'
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['shipping_returns'] = Shipping_returns.objects.all()
        return context


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        messages.info(
            self.request, "Thanks for getting in touch. We have received your message.")
        name = form.cleaned_data.get(_('name'))
        email = form.cleaned_data.get(_('email'))
        message = form.cleaned_data.get(_('message'))

        full_message = f"""
            Received message below from {name}, {email}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)


@login_required(login_url='/login')  # Check login
def savelangcur(request):
    lasturl = request.META.get('HTTP_REFERER')
    curren_user = request.user
    language = Language.objects.get(code=request.LANGUAGE_CODE[0:2])
    # Save to User profile database
    data = UserProfile.objects.get(user_id=curren_user.id)
    data.language_id = language.id
    data.currency_id = request.session['currency']
    data.save()  # save data
    return HttpResponseRedirect(lasturl)
