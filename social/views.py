from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django_filters.views import FilterView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.urls import reverse_lazy
from django import forms

from .models import Link
from .forms import LinkForm
from .filters import LinkListFilter
# Create your views here.


@method_decorator(login_required, name='dispatch')
class LinkUpdateView(UpdateView):
    model = Link
    form_class = LinkForm
    template_name = 'link_update_form.html'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('socialUpdate', args=[self.object.id]) + '?ok'


@method_decorator(login_required, name='dispatch')
class LinkAdminListView(FilterView):
    # Vista para ver la lista de categorias con un de decorador para que solo los administardores puedan acceder
    model = Link
    template_name = 'socialadmin.html'
    context_object_name = 'links'
    ordering = ["name"]
    filterset_class = LinkListFilter

    def get_queryset(self):
        return Link.objects.all()
