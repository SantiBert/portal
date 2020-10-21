from django.shortcuts import render
from django.views.generic.list import View, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django_filters.views import FilterView

from .models import BlogEntry, BlogCategory
from .filters import BlogAdminListFilter
from .forms import BlogEntryForm, BlogCategoryEntryForm

from audit.signals import Audits
from unicodedata import category, category


class BlogEntryListView(ListView):
    # Vista de la lista de posts del Usuario actual
    model = BlogEntry
    # Filtro por blogs activos solamente

    def get_queryset(self):
        new_context = BlogEntry.objects.filter(active=True)
        return new_context


class BlogEntryDetailView(DetailView):
    # Vista del contendido de cada post
    model = BlogEntry


class BlogEntryCategoryList(ListView):

    def get(self, request, slug, *args, **kwargs):
        try:
            posts = BlogEntry.objects.filter(active=True)
            categories = BlogCategory.objects.filter(is_active=True)
            category = BlogCategory.objects.get(slug=slug)
            new_context = BlogEntry.objects.filter(category=category, active=True)
            context = {
                'object_list': new_context,
                'posts': posts,
                'categories': categories,
                'category': category
            }
        except:
            context = {}
        return render(request, 'blog/categories-post.html', context)


@method_decorator(login_required, name='dispatch')
class BlogEntryCreateView(CreateView):
    # Vista para crear los post con un de decorador para que solo los administardores puedan acceder
    model = BlogEntry
    form_class = BlogEntryForm
    success_url = reverse_lazy('administration')

    # Devuelve al usuario actualmente logueado para el campo de User del Blog creado
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogEntryCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class BlogEntryUpdateView(UpdateView):
    # Vista para editar un post creado con un de decorador para que solo los administardores puedan acceder
    model = BlogEntry
    form_class = BlogEntryForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('blog:update', args=[self.object.id]) + '?ok'


@method_decorator(login_required, name='dispatch')
class BlogEntryDeleteView(DeleteView):
    # Vista para borrar los post  con un de decorador para que solo los administardores puedan acceder
    model = BlogEntry
    success_url = reverse_lazy('blog:blogs')


@method_decorator(login_required, name='dispatch')
class BlogCategoryCreate(CreateView):
    # Vista para crear categorias de posts con un de decorador para que solo los administardores puedan acceder
    model = BlogCategory
    form_class = BlogCategoryEntryForm
    success_url = reverse_lazy('administration')


@method_decorator(login_required, name='dispatch')
class BlogCategoryListView(ListView):
    # Vista para ver la lista de categorias con un de decorador para que solo los administardores puedan acceder
    model = BlogCategory


@method_decorator(login_required, name='dispatch')
class BlogCategoryUpdateView(UpdateView):
    # Vista para editar una categoria con un de decorador para que solo los administardores puedan acceder
    model = BlogCategory
    form_class = BlogCategoryEntryForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('blog:categories', args=[self.object.id]) + '?ok'


@method_decorator(login_required, name='dispatch')
class BlogCategoryChangeState(View):
    # Vista para borrar una categoria con un de decorador para que solo los administardores puedan acceder
    # model = BlogCategory
    # success_url = reverse_lazy('blog:blogs')
    def post(self, request, category_id, *args, **kwargs):
        try:
            category = BlogCategory.objects.get(id=category_id)
            category.is_active = not category.is_active
            category.save()
            return HttpResponse("ok", status=200)
        except BlogCategory.DoesNotExist:
            return HttpResponse("Category not found", status=404)
        except:
            return HttpResponse("error code", status=500)


@method_decorator(login_required, name='dispatch')
class BlogAdminListView(FilterView):
    # Vista de la lista de posts para el administrador
    model = BlogEntry
    context_object_name = 'blogs'
    template_name = 'admin/blogadmin-list.html'
    paginate_by = 30  # TODO obtener dato de un constants.py
    filterset_class = BlogAdminListFilter
    ordering = ["name", "user__username", "user__first_name",
                "user__last_name", "category__name", "active", "date"]

    def get_queryset(self):
        return BlogEntry.objects.all()


@method_decorator(login_required, name='dispatch')
class BlogChangeStateView(View):
    # Cambia el estado de un blog, usado en el jquerry de blogadmin-list.html
    def post(self, request, blog_id, *args, **kwargs):
        try:
            blog = BlogEntry.objects.get(id=blog_id)
            blog.active = not blog.active
            blog.save()
            if blog.active:
                audit_description = f"Se activa el Blog :{blog_id}"
            else:
                audit_description = f"Se desactiva el Blog :{blog_id}"
            Audits.audit_action(request.user, "", audit_description, "DELETE")
            return HttpResponse("ok", status=200)
        except BlogEntry.DoesNotExist:
            return HttpResponse("Blog not found", status=404)
        except Exception as e:
            print(e)
            return HttpResponse("error code", status=500)
