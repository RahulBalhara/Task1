"""workshop_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.urls import re_path, include  # <-- IMPORT UPDATED
from django.conf.urls.static import static
from django.contrib import admin
from workshop_portal import views
from django.conf import settings


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),  # <-- url changed to re_path
    re_path(r'^$', views.index),           # <-- url changed to re_path
    re_path(r'^workshop/', include('workshop_app.urls')),  # <-- url changed to re_path
    re_path(r'^reset/', include('django.contrib.auth.urls')),   # <-- url changed to re_path
    re_path(r'^page/', include('cms.urls')),                   # <-- url changed to re_path
    re_path(r'^statistics/', include('statistics_app.urls')), # <-- url changed to re_path
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)