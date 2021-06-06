from django import forms
from .models import Option

class OptionForm(forms.ModelForm):

    class Meta:
        model = Option
        fields = ('name', 'menu',)
        widgets = {
            'menu': forms.HiddenInput(),
        }