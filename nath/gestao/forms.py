from django import forms
from django.core.validators import MinValueValidator
from django.db.models.fields import BLANK_CHOICE_DASH
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field

from home.forms import softdelete_fields

from gestao.models import Laboratorio


class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        exclude = softdelete_fields

    def __init__(self, *args, readonly=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        if readonly:
            self.helper.all().wrap(Field, readonly="readonly", disabled="disabled")
        self.helper.all().wrap(Div, css_class="col-6")
