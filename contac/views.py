from django.shortcuts import render
from django.views.generic.list import View, ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import ContactForm
from .models import Contact
from blog.models import BlogEntry, BlogCategory
# Create your views here.


class ContactFormView(View):
    def get(self, request, *args, **kwargs):
        posts = BlogEntry.objects.filter(active=True)
        categories = BlogCategory.objects.filter(is_active=True)
        form = ContactForm()
        context = {
            'form': form,
            'posts': posts,
            'categories': categories,
        }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                context = {
                    'form': form,
                }
        except:
            context = {}
        return render(request, 'contact.html', context)

@method_decorator(login_required, name='dispatch')
class ContacAdminList(ListView):
    def get(self, request, *args, **kwargs):
        try:
            menssges = Contact.objects.filter(state= True)
            context = {
                'object_list': menssges
            }
        except:
            context = {}
        return render(request, 'contacadminlist.html', context)

@method_decorator(login_required, name='dispatch')
class ConctacAdminDetailView(DetailView):
    model = Contact