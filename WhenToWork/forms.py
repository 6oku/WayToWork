from django import forms
from .models import List, User


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed",]
  
    
        