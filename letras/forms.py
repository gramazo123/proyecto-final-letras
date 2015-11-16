from django import forms
from .models import Banda

class BandaForm(forms.ModelForm):

    class Meta:
        model = Banda
        fields = ('banda', 'integrantes', 'foto',)
