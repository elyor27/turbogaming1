from django.views.generic import ListView, DetailView
from .models import *


class ComputerListView(ListView):
    template_name = 'computers.html'
    paginate_by = 9

    def get_queryset(self):
        qs = ComputerModel.objects.order_by('-pk')
        q = self.request.GET.get('q')

        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        color = self.request.GET.get('color')
        price = self.request.GET.get('price')

        if q:
            qs = qs.filter(title__icontains=q)

        if cat:
            qs = qs.filter(category__id=cat)

        if brand:
            qs = qs.filter(brand__id=brand)

        if color:
            qs = qs.filter(colors__id=color)

        if price:
            price = price.split(';')
            price_from, price_to = price
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['colors'] = ColorModel.objects.all()

        return context


class AccessoriesListView(ListView):
    template_name = 'accessoriescom.html'
    paginate_by = 9

    def get_queryset(self):
        qs = AccessoriesModel.objects.order_by('-pk')
        q = self.request.GET.get('q')

        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        color = self.request.GET.get('color')
        price = self.request.GET.get('price')

        if q:
            qs = qs.filter(title__icontains=q)

        if cat:
            qs = qs.filter(category__id=cat)

        if brand:
            qs = qs.filter(brand__id=brand)

        if color:
            qs = qs.filter(colors__id=color)

        if price:
            price = price.split(';')
            price_from, price_to = price
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['colors'] = ColorModel.objects.all()

        return context


class ComputerDetailView(DetailView):
    model = ComputerModel
    template_name = 'computer_detail.html'


class AccessoriesDetailView(DetailView):
    model = AccessoriesModel
    template_name = 'accessories_com_detail.html'
