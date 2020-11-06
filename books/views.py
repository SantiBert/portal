from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.views.generic.list import View, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .models import BookEntry
from .forms import BookEntryForms
from .filter import BookdminListFilter
from blog.models import BlogEntry, BlogCategory
from core.models import Description
from audit.signals import Audits

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
    template_name = 'bookentry_update_form.html'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('bookupdate', args=[self.object.id]) + '?ok'


@method_decorator(login_required, name='dispatch')
class BookAdminListView(FilterView):
    # Vista de la lista de posts para el administrador
    model = BookEntry
    context_object_name = 'books'
    template_name = 'adminbook.html'
    paginate_by = 30  # TODO obtener dato de un constants.py
    filterset_class = BookdminListFilter
    ordering = ["name"]

    def get_queryset(self):
        return BookEntry.objects.all()


@method_decorator(login_required, name='dispatch')
class BookEntryDeleteView(DeleteView):
    # Vista para borrar los post  con un de decorador para que solo los administardores puedan acceder
    model = BookEntry
    success_url = reverse_lazy('administration')


class BookListView(ListView):
    def get(self, request, *args, **kwargs):
        try:
            posts = BlogEntry.objects.filter(active=True)
            categories = BlogCategory.objects.filter(is_active=True)
            new_context = BookEntry.objects.filter(is_active=True)
            web = Description.objects.filter(is_active=True)
            context = {
                'object_list': new_context,
                'posts': posts,
                'categories': categories,
                'web': web,
            }
        except:
            context = {}
        return render(request, 'bookentry_list.html', context)

    """
    model = BookEntry
    template_name = 'bookentry_list.html'
    """


@method_decorator(login_required, name='dispatch')
class BookChageStateView(View):
    # Cambia el estado de un blog, usado en el jquerry de blogadmin-list.html
    def post(self, request, book_id, *args, **kwargs):
        try:
            book = BookEntry.objects.get(id=book_id)
            book.is_active = not book.is_active
            book.save()
            if book.is_active:
                audit_description = f"Se activa el Sitio :{book_id}"
            else:
                audit_description = f"Se desactiva el Sitio :{book_id}"
            Audits.audit_action(request.user, "", audit_description, "DELETE")
            return HttpResponse("ok", status=200)
        except BookEntry.DoesNotExist:
            return HttpResponse("Sitio not found", status=404)
        except Exception as e:
            print(e)
            return HttpResponse("error code", status=500)
