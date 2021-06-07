from django import forms
from .models import Option, EmployeeOption
from django.conf import settings

class OptionForm(forms.ModelForm):

    class Meta:
        model = Option
        fields = ('name', 'menu',)
        widgets = {
            'menu': forms.HiddenInput(),
        }

class EmployeeOptionForm(forms.ModelForm):

    def clean(self):
        from django.utils import timezone
        form_data = self.cleaned_data
        now = timezone.localtime(timezone.now())
        if now.time() > settings.BOUNDRY_TIME_FOR_REQUEST:
            self._errors["created"] = [f"Time is greater than time permited {settings.BOUNDRY_TIME_FOR_REQUEST}"] # Will raise a error message
        return form_data

    class Meta:
        model = EmployeeOption
        fields = ('menu', 'employee', 'option_selected', 'specification')
        widgets = {
            'menu': forms.HiddenInput(),
            'employee': forms.HiddenInput(),
            'option_selected': forms.HiddenInput(),
        }     