from django import forms
from .models import my_works

class to_do_list(forms.ModelForm):
    class Meta:
        model=my_works
        fields=['title']
