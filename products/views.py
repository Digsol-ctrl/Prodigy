from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        qs = Product.objects.filter(available=True)
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q | qs.filter(description_icontains=q) )
        return qs

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_active and self.request.user.is_staff


class ProductCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'core/product_form.html'


class ProductUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'core/product_form.html'


class ProductDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Product
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('shop:product_list')

    


