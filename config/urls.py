
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('blogs/', include("blog.urls")),
    path('shop/', include("shop.urls")),
    path('gallery/', include("gallery.urls")),
    path('training/', include("training.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
