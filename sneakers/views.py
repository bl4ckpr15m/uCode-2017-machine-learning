from django.core.urlresolvers import reverse_lazy
from django.views import generic
from braces import views

from uCode.settings import twitter_api
from sneakers.forms import PictureForm
from uCode import tasks as tk
from sneakers.models import Sneaker


class SneakersListView(
        views.LoginRequiredMixin,
        views.SetHeadlineMixin,
        generic.ListView):

    headline = 'Sneakers'
    model = Sneaker

    def get_context_data(self, *args, **kwargs):
        context = super(SneakersListView, self).get_context_data(*args, **kwargs)
        sneaker = Sneaker.objects.first()
        context['tweets'] = twitter_api.GetSearch(
                raw_query="q={}&result_type=recent&count=7".format(sneaker.label))

        return context


class IndexView(
        views.LoginRequiredMixin,
        views.SetHeadlineMixin,
        generic.FormView):

    headline = 'Sneakers'
    template_name = "index.html"
    form_class = PictureForm

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def form_valid(self, form):
        feature = form.cleaned_data['feature']
        # tk.predict.delay()
        return super(IndexView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('sneakers:profile')
