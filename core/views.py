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
from django_filters.views import FilterView

from blog.models import BlogEntry, BlogCategory
from contac.models import Contact
from .models import Profile, Description, OtherSites
from .forms import ProfileForm, EmailForm, NameUpdateForm, DescriptionForm, OtherSitesForm
from .filters import OtherSitesListFilter


class IndexView(View):
    def get(self, request, *args, **kwargs):
        try:
            posts = BlogEntry.objects.filter(
                active=True).order_by('-created_date')[:6]
            categories = BlogCategory.objects.filter(is_active=True)
            web = Description.objects.filter(is_active=True)
            #category = BlogCategory.objects.get(slug=slug)
            featured = BlogEntry.objects.filter(
                active=True, featured=True).order_by('-created_date')
            recientes = BlogEntry.objects.filter(
                active=True).order_by('-created_date')
            sites = OtherSites.objects.filter(
                is_active=True)

            context = {
                'posts': posts,
                'categories': categories,
                # 'category': category,
                'featured': featured,
                'sites': sites,
                'recientes': recientes,
                'web': web,
            }
        except:
            context = {}
        return render(request, 'index.html', context)


class LateralView(ListView):
    def get(self, request, *args, **kwargs):
        try:
            featured = BlogEntry.objects.filter(
                active=True, featured=True).order_by('-created_date')
            sites = OtherSites.objects.filter(
                is_active=True)
            context = {
                'sites': sites,
                'featured': featured
            }
        except:
            context = {}
        return render(request, 'includes/lateral.html', context)


class NavbarView(View):
    def get(self, request, *args, **kwargs):
        try:
            categories = BlogCategory.objects.filter(is_active=True)
            context = {
                'categories': categories,
            }
        except:
            context = {}
        return render(request, 'templates/includes/navbar.html', context)


class SearchView(View):
    def get(self, request, *args, **kwargs):
        queryset = request.POST.get("buscar")
        categories = BlogCategory.objects.filter(is_active=True)
        web = Description.objects.filter(is_active=True)
        featured = BlogEntry.objects.filter(
            active=True, featured=True).order_by('-created_date')
        sites = OtherSites.objects.filter(
            is_active=True)
        context = {
            'categories': categories,
            'featured': featured,
            'sites': sites,
            'web': web,
        }

        return render(request, 'results.html', context)

    def post(self, request, *args, **kwargs):
        queryset = request.POST.get("buscar")
        categories = BlogCategory.objects.filter(is_active=True)
        web = Description.objects.filter(is_active=True)
        featured = BlogEntry.objects.filter(
            active=True, featured=True).order_by('-created_date')
        sites = OtherSites.objects.filter(
            is_active=True)
        if queryset:
            posts = BlogEntry.objects.filter(
                Q(name__icontains=queryset) |
                Q(description__icontains=queryset),
                active=True
            ).distinct().order_by('-created_date')

        context = {
            'categories': categories,
            'featured': featured,
            'web': web,
            'sites': sites,
            'object_list': posts,
        }

        return render(request, 'results.html', context)


@method_decorator(login_required, name='dispatch')
class AdministrationView(View):
    def get(self, request, *args, **kwargs):
        total = len(list(Contact.objects.filter(state=True)))
        context = {
            'total': total
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
class AboutUsFormView(UpdateView):
    model = Description
    form_class = DescriptionForm
    success_url = reverse_lazy('administration')
    template_name = 'registration/about_us_form.html'


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


@method_decorator(login_required, name='dispatch')
class OtherSitesCreateView(CreateView):
    # Vista para crear los post con un de decorador para que solo los administardores puedan acceder
    model = OtherSites
    form_class = OtherSitesForm
    success_url = reverse_lazy('administration')
    template_name = 'othersides/othersites_form.html'

    # Devuelve al usuario actualmente logueado para el campo de User del Blog creado
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OtherSitesCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class OtherSitesAdminListView(FilterView):
    # Vista de la lista de posts para el administrador
    model = OtherSites
    context_object_name = 'sites'
    template_name = 'othersides/adminothersites.html'
    paginate_by = 30  # TODO obtener dato de un constants.py
    filterset_class = OtherSitesListFilter
    ordering = ["name"]

    def get_queryset(self):
        return OtherSites.objects.all()


@method_decorator(login_required, name='dispatch')
class OtherSitesUpdateView(UpdateView):
    model = OtherSites
    form_class = OtherSitesForm
    template_name = 'othersides/othersites_update_form.html'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('sitesupdate', args=[self.object.id]) + '?ok'
