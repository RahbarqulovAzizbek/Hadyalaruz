from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from shop.models import ProductModel, CategoryModel


class ShopView(ListView):
    model = ProductModel
    template_name = 'main/shop.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ShopView, self, *args, **kwargs).get_context_data()
        context['categories'] = CategoryModel.objects.all()
        return context

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q)
            return qs
        cat = self.request.GET.get('cat')
        if cat:
            qs = qs.filter(category_id=cat)
        return qs


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'main/product_detail.html'
    context_object_name = 'product'
