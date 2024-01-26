from django import forms
from . import models

class ProfesoForm(forms.ModelForm):
    class Meta:
        model = models.Profesor
        fields = "__all__"