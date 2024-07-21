from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.index_view, name='home'),
    path('agri-drone', views.agri_view, name='agri-detail'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('career', views.career_view, name='career'),
    path('subscribe', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('whatsapp-redirect', views.whatsapp_redirect, name='whatsapp-redirect'),
    path('lang-select', views.set_language, name='set-language'),
]