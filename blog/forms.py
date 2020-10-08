from django import forms

from .models import BlogEntry, BlogCategory


class BlogEntryForm(forms.ModelForm):

    class Meta:
        model = BlogEntry
        fields = ['name', 'description', 'category', 'image_ref']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'name': '', 'description': '', 'category': '', 'image_ref': '',
        }


class BlogCategoryEntryForm(forms.ModelForm):

    class Meta:
        model = BlogCategory
        fields = ['slug', 'name']
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'slug'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
