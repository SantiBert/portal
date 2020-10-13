from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('state',)

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'lastname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo electrónico',
                }
            ),
            'issue': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el asunto',
                }
            ), 'messaje': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su mensaje',
                    'cols': "30",
                    'rows': "10"
                }
            ),
        }
