from .models import Employee
from django.views import generic
from django.urls import reverse_lazy

class EmployeesIndexView(generic.ListView):
    template_name = 'employees/index.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return Employee.objects.order_by('-name')

class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = 'employees/detail.html'

class EmployeeCreateView(generic.CreateView):
    model = Employee
    fields = ['name', 'slack_webhook_url']
    template_name = 'employees/form.html'

class EmployeeUpdateView(generic.edit.UpdateView):
    model = Employee
    fields = ['name', 'slack_webhook_url']
    template_name = 'employees/update.html'
    
class EmployeeDeleteView(generic.DeleteView):
    model = Employee
    template_name = 'employees/confirm_delete.html'
    success_url = reverse_lazy('employees-index') 