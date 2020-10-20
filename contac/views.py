from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from .forms import ContactForm
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
                return redirect('core:index')
            else:
                context = {
                    'form': form,
                }
        except:
            context = {}
        return render(request, 'contact.html', context)
