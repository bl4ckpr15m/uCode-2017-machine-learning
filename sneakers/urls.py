from django.conf.urls import url

from views import IndexView

app_name = 'sneakers'

urlpatterns = [
        url(r'^$', IndexView.as_view(), name='main'),
        ]
