from django.db import models
from django.shortcuts import reverse


class Employee(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200)
    slack_webhook_url = models.URLField(max_length=200)

    def get_absolute_url(self):
        return reverse("employee-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Id {self.id}, {self.name}"
