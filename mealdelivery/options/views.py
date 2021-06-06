from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .forms import OptionForm
from .models import Option
from menus.models import Menu
from django.views import generic

def create(request, menu_pk):
    menu = get_object_or_404(Menu, pk=menu_pk)
    option = Option(menu=menu)
    if request.method == 'POST':
        form = OptionForm(request.POST, instance=option)
        if form.is_valid():
            form.save()
            return redirect('menu-detail', pk=menu.id)
    else:
        form = OptionForm(instance=option)
    return render(request, 'options/create.html', {'form': form, 'menu': menu})

class OptionDetailView(generic.DetailView):
    model = Option
    template_name = 'options/detail.html'

class OptionUpdateView(generic.UpdateView):
    model = Option
    fields = ['name']
    template_name = 'options/update.html'


class OptionDeleteView(generic.DeleteView):
    model = Option
    template_name = 'options/confirm_delete.html'
    success_url = reverse_lazy('menu-index') 