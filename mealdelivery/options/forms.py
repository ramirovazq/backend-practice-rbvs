from django import forms
from .models import Option, EmployeeOption

class OptionForm(forms.ModelForm):

    class Meta:
        model = Option
        fields = ('name', 'menu',)
        widgets = {
            'menu': forms.HiddenInput(),
        }

class EmployeeOptionForm(forms.ModelForm):

    class Meta:
        model = EmployeeOption
        fields = ('menu', 'employee', 'option_selected', 'specification')
        widgets = {
            'menu': forms.HiddenInput(),
            'employee': forms.HiddenInput(),
            'option_selected': forms.HiddenInput(),
        }     