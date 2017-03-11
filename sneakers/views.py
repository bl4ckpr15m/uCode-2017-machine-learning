from django.core.urlresolvers import reverse_lazy
from django.views import generic
from braces import views

from sneakers.forms import PictureForm
from uCode import tasks as tk


class IndexView(
        views.LoginRequiredMixin,
        generic.FormView):

    headline = 'Sneakers'
    template_name = "index.html"
    form_class = PictureForm

    def form_valid(self, form):
        feature = form.cleaned_data['feature']
        print(feature)

    def get_success_url(self, **kwargs):
        return reverse_lazy('sneakers:main')
