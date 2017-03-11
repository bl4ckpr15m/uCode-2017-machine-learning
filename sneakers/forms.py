from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

from sneakers import models


class PictureForm(forms.ModelForm):
    class Meta:
        fields = ('feature',)
        model = models.Sneaker

    def __init__(self, *args, **kwargs):
        super(PictureForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'col-md-9 col-md-offset-1'
        self.helper.layout = Layout(
                'feature',
                ButtonHolder(
                    Submit('send', 'Send', css_class='btn')
                    )
                )

        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
        self.helper.form_show_labels = False
