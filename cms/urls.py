from django.urls import re_path # <-- IMPORT UPDATED

from cms import views

app_name = "cms"

urlpatterns = [
    # This path is for your homepage
    re_path(r'^$', views.home, name='home'), # <-- url changed to re_path

    # This path is for any other page, identified by a permalink
    re_path(r'^(?P<permalink>.+)$', views.home, name='page') # <-- url changed to re_path and name updated
]