from django.db import models
from django.shortcuts import reverse
from menus.models import Menu
from employees.models import Employee

class Option(models.Model):
    name = models.CharField(
            blank=True,
            null=True,
            max_length=100,
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.PROTECT,
        db_index=True
    )
    created = models.DateField(
        auto_now_add=True,
    )


    def get_absolute_url(self):
        return reverse('option-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.menu}: {self.name}" 


class EmployeeOption(models.Model):
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
    option_selected = models.ForeignKey(
        Option,
        on_delete=models.PROTECT,
        db_index=True
    )
    specification = models.TextField(
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.menu} {self.employee} {self.option_selected}"