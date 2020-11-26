from django import forms
from .models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url']

        widgets = {
            'url': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el link de la red social',
                }
            ),
        }
