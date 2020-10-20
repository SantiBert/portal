from django import forms
from .models import BookEntry


class BookEntryForms(forms.ModelForm):
    class Meta:
        model = BookEntry
        fields = '__all__'
        exclude = ('is_active',)

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el título',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su la descripción',

                }
            ),
        }
