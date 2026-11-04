from django import forms
from .models import Escuderia


class EscuderiaForm(forms.ModelForm):

    class Meta:
        model = Escuderia
        fields = [
            'nombre',
            'pais',
            'logo',
            'informacion'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'pais': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'logo': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'informacion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
        }