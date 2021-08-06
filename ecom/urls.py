from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import views
from django.utils.translation import gettext_lazy as _
from marketing.views import email_list_signup
from core.views import (
    change_language,
    Shipping_returnsListView,
    FaqListView,
    Terms_of_useListView,

    )

urlpatterns = [
    path('change_language/',change_language,name='change_language'),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path(_('accounts/'), include('allauth.urls')),
    path('', views.home, name='home'),
    path(_('about/'), views.AboutListView.as_view(), name='about'),
    path(_('privacy_policy/'), views.Privacy_policyListView.as_view(), name='privacy_policy'),
    path(_('shipping_returns/'), Shipping_returnsListView.as_view(), name='shipping_returns'),
    path(_('contact/'), views.ContactView.as_view(), name='contact'),
    path(_('faq/'), FaqListView.as_view(), name='faq'),
    path(_('terms_of_use/'), Terms_of_useListView.as_view(), name='terms_of_use'),
    path(_('cart/'), include('cart.urls', namespace='cart')),
    path(_('staff/'), include('staff.urls', namespace='staff')),
    path(_('profile/'), views.ProfileView.as_view(), name='profile'),
    path('_ckeditor/', include('ckeditor_uploader.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('email-signup/', email_list_signup, name='email-list-signup'),
    
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
