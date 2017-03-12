from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include
from rest_framework import routers

from uCode import views


router = routers.DefaultRouter()
router.register(r'sneakers', views.SneakersViewSet)

urlpatterns = [
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^api/', include(router.urls, namespace='sneakers_api')),
        url(r'^', include('sneakers.urls'), name="sneakers"),
        url(r'^admin/', admin.site.urls, name='admin'),
        url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
        url(r'^login/$', views.LoginView.as_view(), name='login'),
        ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
