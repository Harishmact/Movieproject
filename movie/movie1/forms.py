from django import forms
from movie1.models import mnames

class mforms(forms.ModelForm):
    class Meta:
        model=mnames
        fields='__all__'
