from django.contrib import admin
from django.urls import path, include
from s3 import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('s3/', include(urls))
]
