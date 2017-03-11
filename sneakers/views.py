from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from braces import views

# from sneakers.forms import PictureForm
from uCode import tasks as tk


class IndexView(
        views.LoginRequiredMixin,
        generic.TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
