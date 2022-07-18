from django import forms
from django.forms import ModelForm

from dashboard.utils import receipt_no
from .models import offloadedCargo



class ReceiveGoodsForm(forms.ModelForm):
    class Meta:
        model = offloadedCargo 
        fields = (
            'container_origin','container_number','client_name','sales_agent','goods','cbm','ctns','weight','remarks',
        )
        widgets = {

            'container_origin': forms.Select(attrs={
                'class':'form-control'
            }),
            'container_number': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'client_name': forms.Select(attrs={
                'class':'form-control'
            }),
            'sales_agent': forms.Select(attrs={
                'class':'form-control'
            }),
            'goods': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'cbm': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'ctns': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'weight': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'remarks': forms.Textarea(attrs={
                'class':'form-control'
            }),
            
        }