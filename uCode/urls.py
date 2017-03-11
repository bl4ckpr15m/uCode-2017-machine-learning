from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include
from rest_framework import routers

from .views import LoginView, LogoutView

router = routers.DefaultRouter()

urlpatterns = [
        url(r'^admin/', admin.site.urls, name='admin'),
        url(r'^logout/$', LogoutView.as_view(), name='logout'),
        url(r'^$', include('sneakers.urls'), name="sneakers"),
        url(r'^login/$', LoginView.as_view(), name='login'),
        url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^api/v1/', include(router.urls, namespace='api')),
        ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
