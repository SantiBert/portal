from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django import forms

from blog.models import BlogEntry, BlogCategory
from contac.models import Contact
from .models import Profile
from .forms import ProfileForm, EmailForm, NameUpdateForm


class IndexView(View):
    def get(self, request,*args, **kwargs):
        try:
            posts = BlogEntry.objects.filter(active=True)
            categories = BlogCategory.objects.filter(is_active=True)
            about = Profile.objects.all()
            context = {
                'posts': posts,
                'categories': categories,
                'about':about
            }
        except:
            context = {}
        return render(request, 'index.html', context)

class SearchView(View):
    def post(self, request, *args, **kwargs):
        queryset = request.POST.get("buscar")
        if queryset:
            posts = BlogEntry.objects.filter(
                Q(name__icontains=queryset) |
                Q(description__icontains=queryset),
                active=True
            ).distinct()

        return render(request, 'results.html', {'object_list': posts})


@method_decorator(login_required, name='dispatch')
class AdministrationView(View):
    def get(self, request, *args, **kwargs):
        total = len(list(Contact.objects.filter(state=True)))
        context = {
            'total':total
        }
        return render(request, "administration.html", context)


@method_decorator(login_required, name='dispatch')
# Actualiza o crea los datos de un usuario para un perfil
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(
            user=self.request.user)
        return profile


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):  # Permite editar el e-mail de un usuario
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        return form


@method_decorator(login_required, name='dispatch')
class NameUpdate(UpdateView):  # Permite editar el e-mail de un usuario
    form_class = NameUpdateForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_name_form.html'

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(NameUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['first_name'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre'})
        form.fields['last_name'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Apellido'})
        return form
