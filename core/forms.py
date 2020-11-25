from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile, Description, OtherSites, Quote, FriendSites


class ProfileForm(forms.ModelForm):  # Formulario para editar perfil

    class Meta:
        model = Profile
        fields = ['image', 'description']
        widgets = {
            'image': forms.ClearableFileInput(),
            # 'phone': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Numero de telefono'}),
            'description': forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'Descripción'})
        }


class EmailForm(forms.ModelForm):  # Formulario para editar email
    email = forms.EmailField(
        required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' == self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "El e-mail ya está registrado, prueba con otro.")
        return email


class NameUpdateForm(forms.ModelForm):  # Formulario para editar nombre y apellido

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class DescriptionForm(forms.ModelForm):

    class Meta:
        model = Description
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'Quienes somos'})
        }


class OtherSitesForm(forms.ModelForm):
    class Meta:
        model = OtherSites
        fields = '__all__'
        exclude = ('active',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
        }


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'
        exclude = ('active',)
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor'}),
            'book': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Libro'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Cita'}),
        }


class FriendSitesForm(forms.ModelForm):
    class Meta:
        model = FriendSites
        fields = '__all__'
        exclude = ('active',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'site_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del sitio'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
        }
