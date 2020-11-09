import random
from django.shortcuts import render
from django.views.generic.list import View, ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib.auth.models import User

from .forms import ContactForm
from .models import Contact
from blog.models import BlogEntry, BlogCategory
from core.models import Profile, Description, Quote
# Create your views here.


class ContactFormView(View):
    def get(self, request, *args, **kwargs):
        posts = BlogEntry.objects.filter(active=True)
        categories = BlogCategory.objects.filter(is_active=True)
        web = Description.objects.filter(is_active=True)
        form = ContactForm()
        person = User.objects.all(),
        quotes = Quote.objects.filter(active=True)
        context = {
            'form': form,
            'posts': posts,
            'quote': random.choice(quotes),
            'categories': categories,
            'person': person,
            'web': web,
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
            menssges = Contact.objects.filter(state=True)
            context = {
                'object_list': menssges
            }
        except:
            context = {}
        return render(request, 'contacadminlist.html', context)


@method_decorator(login_required, name='dispatch')
class ConctacAdminDetailView(DetailView):
    model = Contact
    template_name = 'contact_detail.html'


@method_decorator(login_required, name='dispatch')
class ContactChangeStateView(View):
    def post(self, request, contact_id, *args, **kwargs):
        try:
            contact = Contact.objects.get(id=contact_id)
            contact.state = not contact.state
            contact.save()
            return HttpResponse("ok", status=200)
        except Contact.DoesNotExist:
            return HttpResponse("Category not found", status=404)
        except:
            return HttpResponse("error code", status=500)
