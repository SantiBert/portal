import random
from django.shortcuts import render
from django.views.generic.list import View, ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.mail import send_mail
from django_filters.views import FilterView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify


from .models import BlogEntry, BlogCategory
from .filters import BlogAdminListFilter
from .forms import BlogEntryForm, BlogCategoryEntryForm
from newportal.settings.local_settings import EMAIL_HOST_USER, SITE_URL_DETAIL

from audit.signals import Audits
from unicodedata import category, category
from core.models import Description, OtherSites, Quote, Suscriptor, FriendSites, Music


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
    template_name = 'blog/blogentry_detail.html'
    slug_field = 'pk'

    def get_context_data(self, **kwargs):
        context = super(BlogEntryDetailView, self).get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.filter(is_active=True)
        context['web'] = Description.objects.filter(is_active=True)
        context['featured'] = BlogEntry.objects.filter(
            active=True, featured=True).order_by('-created_date')
        context['sites'] = OtherSites.objects.filter(
            active=True).order_by('name')
        context['quote'] = random.choice(Quote.objects.filter(active=True))
        context['music'] = Music.objects.filter(is_active=True)
        # other code
        return context


class BlogEntryCategoryList(ListView):

    def get(self, request, slug, *args, **kwargs):
        try:
            posts = BlogEntry.objects.filter(active=True)
            category = BlogCategory.objects.get(slug=slug)
            categories = BlogCategory.objects.filter(is_active=True)
            featured = BlogEntry.objects.filter(
                active=True, featured=True).order_by('-created_date')
            page = request.GET.get('page', 1)
            new_context = BlogEntry.objects.filter(
                category=category, active=True).order_by('-created_date')
            paginator = Paginator(new_context, 10)
            web = Description.objects.filter(is_active=True)
            sites = OtherSites.objects.filter(
                active=True).order_by('name')
            music = Music.objects.filter(is_active=True)
            quotes = Quote.objects.filter(active=True)
            friendsites = FriendSites.objects.filter(
                active=True).order_by('-date')[:5]

        except:
            quotes = None
            posts = None
            category = None
            categories = None
            featured = None
            page = request.GET.get('page', 1)
            new_context = None
            paginator = None
        try:
            new_context = paginator.page(page)
        except:
            context = {}

        context = {
            'object_list': new_context,
            'posts': posts,
            'categories': categories,
            'category': category,
            'sites': sites,
            'featured': featured,
            'music':music,
            'web': web,
            'quote': random.choice(quotes),
            'friendsites': friendsites,
        }
        return render(request, 'blog/categories-post.html', context)


@method_decorator(login_required, name='dispatch')
class BlogEntryCreateView(CreateView):

    model = BlogEntry
    form_class = BlogEntryForm
    success_url = reverse_lazy('administration')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        slug = slugify(form.instance.name, allow_unicode=True)
        pk_url = form.instance.id
        link = SITE_URL_DETAIL + str(pk_url) + '/' + slugify(slug)
        asunto = form.instance.name
        mensaje = 'He publicado un nuevo articulo, ' + \
            form.instance.name + ' puedes leerlo aquí: ' + link
        qs = Suscriptor.objects.filter(active=True)
        for suscriptor in qs:
            try:
                send_mail(asunto, mensaje, EMAIL_HOST_USER,
                          [suscriptor.email, ])
            except:
                pass
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
    success_url = reverse_lazy('blog:listcategories')


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
    paginate_by = 12  # TODO obtener dato de un constants.py
    filterset_class = BlogAdminListFilter
    ordering = ["name", "user__username", "user__first_name",
                "user__last_name", "category__name", "active", "date", "created_date"]

    def get_queryset(self):
        return BlogEntry.objects.all().order_by('-created_date')


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


@method_decorator(login_required, name='dispatch')
class BlogChangeFeaturedView(View):
    # Cambia el estado de un blog, usado en el jquerry de blogadmin-list.html
    def post(self, request, blog_id, *args, **kwargs):
        try:
            blog = BlogEntry.objects.get(id=blog_id)
            blog.featured = not blog.featured
            blog.save()
            if blog.featured:
                audit_description = f"El blog esta en destacados :{blog_id}"
            else:
                audit_description = f"El blog no esta en destacados :{blog_id}"
            Audits.audit_action(request.user, "", audit_description, "DELETE")
            return HttpResponse("ok", status=200)
        except BlogEntry.DoesNotExist:
            return HttpResponse("Blog not found", status=404)
        except Exception as e:
            print(e)
            return HttpResponse("error code", status=500)


class SearchTagView(View):
    def get(self, request, tag, *args, **kwargs):
        queryset = tag
        categories = BlogCategory.objects.filter(is_active=True)
        web = Description.objects.filter(is_active=True)
        featured = BlogEntry.objects.filter(
            active=True, featured=True).order_by('-created_date')
        sites = OtherSites.objects.filter(
            active=True).order_by('name')
        quotes = Quote.objects.filter(active=True)
        if queryset:
            posts = BlogEntry.objects.filter(
                Q(name__icontains=queryset) |
                Q(description__icontains=queryset),
                active=True
            ).distinct().order_by('-created_date')

        context = {
            'categories': categories,
            'featured': featured,
            'quote': random.choice(quotes),
            'web': web,
            'sites': sites,
            'object_list': posts,
        }

        return render(request, 'results.html', context)
