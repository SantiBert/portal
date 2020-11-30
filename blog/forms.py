from django import forms
from datetime import date
from taggit.forms import TagWidget

from .models import BlogEntry, BlogCategory


class BlogEntryForm(forms.ModelForm):

    class Meta:
        model = BlogEntry
        fields = ['name', 'description', 'category',
                  'image_ref', 'featured', 'tags']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.CheckboxSelectMultiple(attrs={'class': 'custom-control custom-radio custom-control-inline'}),
            'featured': forms.CheckboxInput(),
            'tags': TagWidget(),
        }
        labels = {
            'name': '', 'description': '', 'category': '', 'featured': '', 'image_ref': '',
        }


class BlogCategoryEntryForm(forms.ModelForm):

    class Meta:
        model = BlogCategory
        fields = ['slug', 'name']
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'slug'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
