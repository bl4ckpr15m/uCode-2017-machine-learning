from braces import views
from django.views.generic import UpdateView
from django.utils.translation import ugettext_lazy as _

from . import forms
from . import models


class RestrictToOwnerMixin(views.LoginRequiredMixin):
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class ProfileUpdateView(
        RestrictToOwnerMixin,
        views.SetHeadlineMixin,
        views.FormMessagesMixin,
        UpdateView):

    headline = 'Profile'
    form_class = forms.ProfileForm
    model = models.Profile
    form_invalid_message = _(u'There was an error in the process')

    def get_form_valid_message(self):
        return u"""You have just change your personal information
               """
