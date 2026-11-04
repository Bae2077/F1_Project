from django import forms
from .models import Piloto, ParticipacionPiloto

class PilotoForm(forms.ModelForm):

    class Meta:
        model = Piloto
        fields = [
            'nombre',
            'nacionalidad',
            'foto',
            'informacion'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'nacionalidad': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'foto': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'informacion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
        }

class ParticipacionPilotoForm(forms.ModelForm):

    class Meta:
        model = ParticipacionPiloto
        fields = [
            'piloto',
            'escuderia',
            'temporada',
            'numero'
        ]

        widgets = {
            'piloto': forms.Select(attrs={
                'class': 'form-select'
            }),
            'escuderia': forms.Select(attrs={
                'class': 'form-select'
            }),
            'temporada': forms.Select(attrs={
                'class': 'form-select'
            }),
            'numero': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }