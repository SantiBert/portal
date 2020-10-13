from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from .forms import ContactForm
# Create your views here.


class ContactFormView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form,
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
