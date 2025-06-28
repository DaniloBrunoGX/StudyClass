from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

DEBUG = settings.DEBUG
STATIC_URL = settings.STATIC_URL
STATIC_ROOT = settings.STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('socialapp.urls')),
    path('', include('usuario.urls')),
]
if DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)