from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import View, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import BookEntry
from .forms import BookEntryForms

# Create your views here.


@method_decorator(login_required, name='dispatch')
class BookEntryCreateView(CreateView):
    # Vista para crear los post con un de decorador para que solo los administardores puedan acceder
    model = BookEntry
    form_class = BookEntryForms
    template_name = 'bookentry_form.html'
    success_url = reverse_lazy('administration')

    # Devuelve al usuario actualmente logueado para el campo de User del Blog creado
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookEntryCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class BookEntryUpdateView(UpdateView):
    model = BookEntry
    form_class = BookEntryForms
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('administration', args=[self.object.id]) + '?ok'


@method_decorator(login_required, name='dispatch')
class BookAdminListView(ListView):
    # Vista de la lista de posts para el administrador
    model = BookEntry
    template_name = 'adminbook.html'


@method_decorator(login_required, name='dispatch')
class BookEntryDeleteView(DeleteView):
    # Vista para borrar los post  con un de decorador para que solo los administardores puedan acceder
    model = BookEntry
    success_url = reverse_lazy('administration')


class BookListView(ListView):
    model = BookEntry
    template_name = 'bookentry_list.html'
