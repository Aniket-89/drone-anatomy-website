from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.index_view, name='home'),
    path('agri-drone', views.agri_view, name='agri-detail'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('career', views.career_view, name='career'),
    path('mapping', views.mapping_view, name='mapping'),
    path('thrustbench', views.tb_view, name='tb'),
    path('uav-data-processing', views.uav_data_processing_view, name='uav-data-processing'),
    path('subscribe', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('whatsapp-redirect', views.whatsapp_redirect, name='whatsapp-redirect'),
    path('lang-select', views.set_language, name='set-language'),
    path('upcoming', views.upcoming_view, name='upcoming-page'),
]