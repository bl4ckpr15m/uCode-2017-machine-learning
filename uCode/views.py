from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from braces import views
from rest_framework import viewsets

from uCode.forms import LoginForm
from uCode import tasks as tk
from sneakers.models import Sneaker
from .serializers import SneakerSerializer


class LoginView(
        views.AnonymousRequiredMixin,
        views.SetHeadlineMixin,
        generic.FormView):

    form_class = LoginForm
    headline = 'Login'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('sneakers:main')


class LogoutView(
        views.LoginRequiredMixin,
        generic.RedirectView):

    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class SneakersViewSet(viewsets.ModelViewSet):
    queryset = Sneaker.objects.all().order_by('-created_at')
    serializer_class = SneakerSerializer
