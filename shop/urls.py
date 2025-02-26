from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('', views.shop_list_view, name='shop'),
]