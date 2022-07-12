from django.shortcuts import reverse
from django.views.generic import TemplateView, CreateView
from pages.forms import ContactModelForm


class HomePageView(TemplateView):
    template_name = 'main/index.html'

class ContactView(CreateView):
    form_class = ContactModelForm
    template_name = 'main/contact.html'

    def get_success_url(self):
        return reverse('pages:contact')
