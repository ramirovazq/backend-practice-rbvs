from django.shortcuts import redirect
from .models import Menu
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'menus/index.html'
    context_object_name = 'menus'

    def get_queryset(self):
        return Menu.objects.order_by('-created')

class DetailView(generic.DetailView):
    model = Menu
    template_name = 'menus/detail.html'

def create(request):
    context = {}
    menu = Menu.objects.create()
    context['menu'] = menu
    return redirect('menu-detail', pk=menu.id)

class MenuUpdateView(generic.edit.UpdateView):
    model = Menu
    fields = ['active']
    template_name = 'menus/update.html'
    
