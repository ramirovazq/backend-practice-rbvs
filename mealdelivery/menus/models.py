from django.db import models
from django.shortcuts import reverse

class Menu(models.Model):
    created = models.DateField(
        auto_now_add=True,
    )
    active = models.BooleanField(
        default=False
    )

    def get_absolute_url(self):
        return reverse('menu-detail', kwargs={'pk': self.pk})

    def related_options(self):
        from options.models import Option
        return Option.objects.filter(menu=self).order_by('-created')



    def __str__(self):
        return f"Id {self.id}, {self.created.strftime('%d/%m/%Y')}" 
