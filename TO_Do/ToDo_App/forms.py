from ToDo_App.models import Task
from django import forms

class TODoform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','Tdate']