from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

admin.autodiscover()


urlpatterns = [
    path('', include('misc.urls', namespace='misc')),
    path(r'', include('meetups.urls', namespace='meetups')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
