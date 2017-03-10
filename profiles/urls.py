from django.conf.urls import url

from . import views

app_name = 'profile'

urlpatterns = [
        url(r'^(?P<pk>[0-9]+)', views.ProfileUpdateView.as_view(), name='index'),
        ]
