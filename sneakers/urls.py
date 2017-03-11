from django.conf.urls import url

from sneakers.views import IndexView, SneakersListView

app_name = 'sneakers'

urlpatterns = [
        url(r'^$', IndexView.as_view(), name='main'),
        url(r'^profile/$', SneakersListView.as_view(), name='profile'),
        ]
