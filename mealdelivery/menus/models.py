from django.db import models
from django.shortcuts import reverse
from employees.models import Employee
import uuid

class Menu(models.Model):
    created = models.DateField(
        auto_now_add=True,
    )
    date_menu = models.DateField(
        blank=False,
        null=False
    )
    active = models.BooleanField(
        default=False
    )

    def get_absolute_url(self):
        return reverse('menu-detail', kwargs={'pk': self.pk})

    def related_options(self):
        from options.models import Option
        return Option.objects.filter(menu=self).order_by('-created')

    def employees_have_selected(self):
        from options.models import EmployeeOption
        return EmployeeOption.objects.filter(menu=self).order_by('employee')



    def __str__(self):
        return f"Id {self.id}, {self.created.strftime('%d/%m/%Y')}" 

class MenuLinkperEmployee(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.PROTECT,
        db_index=True
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        db_index=True
    )
    url_uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False)

    def options_selected(self):
        from options.models import EmployeeOption
        return EmployeeOption.objects.filter(
            menu=self.menu,
            employee=self.employee
        )

    class Meta:
        unique_together = ['menu', 'employee']


    def __str__(self):
        return f"{self.menu} {self.employee} {self.url_uuid}" 