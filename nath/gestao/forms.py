from django import forms
from django.core.validators import MinValueValidator
from django.db.models.fields import BLANK_CHOICE_DASH
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field

from home.forms import softdelete_fields, EMPTY_LABEL

from gestao.models import Laboratorio, Projeto, Especie, MaterialBiologico


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


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        exclude = softdelete_fields

    def __init__(self, *args, readonly=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        if readonly:
            self.helper.all().wrap(Field, readonly="readonly", disabled="disabled")
        self.helper.all().wrap(Div, css_class="col-6")


class EspecieForm(forms.ModelForm):
    class Meta:
        model = Especie
        exclude = softdelete_fields

    def __init__(self, *args, readonly=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        if readonly:
            self.helper.all().wrap(Field, readonly="readonly", disabled="disabled")
        self.helper.all().wrap(Div, css_class="col-6")


class MaterialBiologicoForm(forms.ModelForm):
    projeto_pk = forms.ModelChoiceField(
        queryset=Projeto.objects.all(), label="Projeto", empty_label=EMPTY_LABEL, required=True
    )
    
    class Meta:
        model = MaterialBiologico
        exclude = softdelete_fields + ["created_by"]
        widgets = {
            'data_coleta': forms.TextInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, readonly=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        if readonly:
            self.helper.all().wrap(Field, readonly="readonly", disabled="disabled")
        self.helper.all().wrap(Div, css_class="col-6")
