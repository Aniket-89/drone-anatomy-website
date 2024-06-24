from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.index_view, name='home'),
    path('agri-drone', views.agri_view, name='agri-detail'),
]