"""workshop_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path # <-- IMPORT UPDATED
from workshop_app import views

app_name = "workshop_app"

urlpatterns = [
    re_path(r'^$', views.index, name='index'), # <-- url changed to re_path
    re_path(r'^register/$', views.user_register, name="register"), # <-- url changed to re_path
    re_path(r'^activate_user/(?P<key>.+)$', views.activate_user), # <-- url changed to re_path
    re_path(r'^activate_user/$', views.activate_user), # <-- url changed to re_path
    re_path(r'^login/$', views.user_login, name="login"), # <-- url changed to re_path
    re_path(r'^logout/$', views.user_logout, name="logout"), # <-- url changed to re_path
    re_path(r'^status$', views.workshop_status_coordinator, # <-- url changed to re_path
        name='workshop_status_coordinator'),
    re_path(r'^dashboard$', views.workshop_status_instructor, # <-- url changed to re_path
        name='workshop_status_instructor'),
    re_path(r'^accept_workshop/(?P<workshop_id>\d+)', views.accept_workshop, # <-- url changed to re_path
        name='accept_workshop'),
    re_path(r'^change_workshop_date/(?P<workshop_id>\d+)$', # <-- url changed to re_path
        views.change_workshop_date, name='change_workshop_date'),
    re_path(r'^details/(?P<workshop_id>\d+)$', views.workshop_details, # <-- url changed to re_path
        name='workshop_details'),
    re_path(r'^type_details/(?P<workshop_type_id>\d+)$', # <-- url changed to re_path
        views.workshop_type_details, name='workshop_type_details'),
    re_path(r'^type_tnc/(?P<workshop_type_id>\d+)$', # <-- url changed to re_path
        views.workshop_type_tnc, name='workshop_type_tnc'),
    re_path(r'^propose/$', views.propose_workshop, # <-- url changed to re_path
        name='propose_workshop'),
    re_path(r'^add_workshop_type$', views.add_workshop_type, # <-- url changed to re_path
        name='add_workshop_type'),
    re_path(r'^delete_attachment_file/(?P<file_id>\d+)$', # <-- url changed to re_path
        views.delete_attachment_file, name='delete_attachment_file'),
    re_path(r'^types/$', views.workshop_type_list, # <-- url changed to re_path
        name='workshop_type_list'),
    re_path(r'^view_profile/$', views.view_own_profile, # <-- url changed to re_path
        name='view_own_profile'),
    re_path(r'^view_profile/(?P<user_id>\d+)$', views.view_profile, # <-- url changed to re_path
        name='view_profile'),
]