from django.shortcuts import redirect, render, get_object_or_404
from .models import Menu, MenuLinkperEmployee
from options.models import EmployeeOption, Option
from employees.models import Employee
from django.views import generic
from options.forms import EmployeeOptionForm

class IndexView(generic.ListView):
    template_name = 'menus/index.html'
    context_object_name = 'menus'

    def get_queryset(self):
        return Menu.objects.order_by('-id')

class DetailView(generic.DetailView):
    model = Menu
    template_name = 'menus/detail.html'

def create(request):
    context = {}
    menu = Menu.objects.create()
    context['menu'] = menu
    return redirect('menu-detail', pk=menu.id)

class MenuCreateView(generic.CreateView):
    model = Menu
    fields = ['date_menu']
    template_name = 'menus/form.html'


class MenuUpdateView(generic.edit.UpdateView):
    model = Menu
    fields = ['active']
    template_name = 'menus/update.html'
    
def menu_link(request, uuid):
    menulink = get_object_or_404(MenuLinkperEmployee, url_uuid=uuid)
    return render(request, "menus/link.html", context={'menulink': menulink})

def menu_select_option(request, uuid, option_id):
    menulink = get_object_or_404(MenuLinkperEmployee, url_uuid=uuid)
    option = get_object_or_404(Option, id=option_id)

    employee_option = EmployeeOption(
        menu=menulink.menu,
        employee=menulink.employee,
        option_selected=option,
        )
    if request.method == 'POST':
        form = EmployeeOptionForm(request.POST, instance=employee_option)
        if form.is_valid():
            form.save()
            return redirect('menu-link', uuid=menulink.url_uuid)
    else:
        form = EmployeeOptionForm(instance=employee_option)

    return render(request, "menus/select.html", context={'form': form, 'menulink': menulink, 'option': option})

def menu_delete_option(request, uuid, employee_option_id):
    menulink = get_object_or_404(MenuLinkperEmployee, url_uuid=uuid)
    employee_option = get_object_or_404(EmployeeOption, id=employee_option_id)
    employee_option.delete()
    return redirect('menu-link', uuid=menulink.url_uuid)
