from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    perfil = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Perfil'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'perfil']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for campo in self.fields:
            if campo != 'perfil':
                self.fields[campo].widget.attrs.update({
                    'class': 'form-control'
                })

    def save(self, commit=True):
        usuario = super().save(commit=commit)

        if commit:
            usuario.email = self.cleaned_data['email']
            usuario.save()
            usuario.groups.clear()
            usuario.groups.add(self.cleaned_data['perfil'])

        return usuario