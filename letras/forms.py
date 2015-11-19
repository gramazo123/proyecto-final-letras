from django import forms
from .models import Banda
from .models import Cancione

class BandaForm(forms.ModelForm):

    class Meta:
        model = Banda
        fields = ('banda', 'integrantes', 'foto',)

class CancionForm(forms.ModelForm):

    class Meta:
        model = Cancione
        fields = ('titulo', 'duracion', 'letra',)

class CancionBForm(forms.ModelForm):
    
    class Meta:
        model = Cancione
        fields = ('banda', 'titulo', 'duracion', 'letra',)

