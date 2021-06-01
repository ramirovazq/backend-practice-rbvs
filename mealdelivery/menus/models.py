from django.db import models

class Menu(models.Model):
    created = models.DateField(
        auto_now_add=True,
        unique=True
    )
    active = models.BooleanField(
        default=False
    )

class Option(models.Model):
    option = models.CharField(
            blank=True,
            null=True,
            max_length=100,
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.PROTECT,
        db_index=True)

