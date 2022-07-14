from django.shortcuts import reverse
from django.views.generic import TemplateView, CreateView

from blog.models import BlogPostModel
from pages.forms import ContactModelForm
from pages.models import BannerModel


class HomePageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self, **kwargs).get_context_data()
        context['last_posts'] = BlogPostModel.objects.all().order_by('-pk')[:4]
        context['banners'] = BannerModel.objects.filter(is_active=True).order_by('-id')
        return context


class ContactView(CreateView):
    form_class = ContactModelForm
    template_name = 'main/contact.html'

    def get_success_url(self):
        return reverse('pages:contact')


class AboutView(TemplateView):
    template_name = 'main/about.html'