from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from products.models import Product
from .models import Project

class Homepage(TemplateView):

    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(available = True)[:3]        
        context['projects'] = Project.objects.all()[:6]
        return context
    
class Projectslist(ListView):
    model = Project
    template_name = "core/projects_list.html"
    context_object_name = 'projects'
    paginate_by = 12

    


