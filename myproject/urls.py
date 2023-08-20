from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onlinecourse/', include('onlinecourse.urls')),
    path('', include('onlinecourse.urls')),  # Add this line for the root URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
