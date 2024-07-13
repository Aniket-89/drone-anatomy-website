from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='bloglist'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blogdetail'),
    path('upload_image/', views.upload_image, name='upload_image'),
]