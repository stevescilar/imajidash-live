from django import forms
from django.forms import ModelForm

from dashboard.utils import receipt_no
from .models import Client, SalesAgent , DispatchCargoChina, ReceivedCargoKenya, Remark ,ReceivedCargoChina,DispatchCargoKenya,ReceivedCargoYiwu,DispatchCargoYiwu 

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'name','contact','sales_agent'
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'contact': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'sales_agent': forms.Select(attrs={
                'class':'form-control'
            }),
        }
class SalesAgentForm(ModelForm):
    class Meta:
       model =  SalesAgent
       fields = (
           'name','contact'
       )
       widgets = {
           'name': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'contact': forms.TextInput(attrs={
                'class':'form-control'
            }),
       }

class RemarkForm(ModelForm):
    class Meta:
        model = Remark
        fields = '__all__'
       

# ------------------------------------------China Warehouse Logic---------------------------------------------#
# ------------------------------------------YIWU Receive Cargo---------------------------------------------#
class CargoFormYiwu(forms.ModelForm):
    class Meta:
        model = ReceivedCargoYiwu 
        fields = (
            'client_name','goods','cbm','ctns','weight','remark',
        )
        widgets = {
            'client_name': forms.Select(attrs={
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
            'remark': forms.Textarea(attrs={
                'class':'form-control'
            }),
            
        }
# ------------------------------------------YIWU Load Cargo---------------------------------------------#
class dispatchFormYiwu(forms.ModelForm):
    class Meta:
        model = DispatchCargoYiwu
        # fields=(
        #     'client_name',
        #     'goods','cbm',
        #     'ctns',
        #     'weight',
        #     'container_number',
        #     'remark',
        # )
        # widgets = {
        #    'client_name': forms.Select(attrs={
        #         'class':'form-control'
        #     }),
        #     'cbm': forms.TextInput(attrs={
        #         'class':'form-control'
        #     }),
        #     'goods': forms.Select(attrs={
        #         'class':'form-control'
        #     }),
        #     'container_number': forms.TextInput(attrs={
        #         'class':'form-control'
        #     }),
        #     'ctns': forms.TextInput(attrs={
        #         'class':'form-control'
        #     }),
        #     'remark': forms.Textarea(attrs={
        #         'class':'form-control'
        #     }),
        #      'weight': forms.TextInput(attrs={
        #         'class':'form-control'
        #     }),
        # }
        fields=(
            'client_name','receipt_no',
            'goods','cbm',
            'ctns',
            'weight',
            'shipping_mark',
            'container_number',
            'remark',
        )
        widgets = {
           'client_name': forms.Select(attrs={
                'class':'form-control'
            }),
            'receipt_no': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'shipping_mark': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'cbm': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'goods': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'container_number': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'ctns': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'remark': forms.Textarea(attrs={
                'class':'form-control'
            }),
             'weight': forms.TextInput(attrs={
                'class':'form-control'
            }),
        }

#-------------------------------------------separation of matters --------------------------------------#
# ------------------------------------------China---------------------------------------------#
class CargoFormChina(forms.ModelForm):
    class Meta:
        model = ReceivedCargoChina 
        fields = (
            'client_name','goods','cbm','ctns','weight','remark',
        )
        widgets = {
            'client_name': forms.Select(attrs={
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
            'remark': forms.Textarea(attrs={
                'class':'form-control'
            }),
            
        }

# --------------------------------------------Dispatching China------------------------------------------#
class dispatchFormChina(forms.ModelForm):
    class Meta:
        model = DispatchCargoChina
        fields=(
            'client_name','receipt_no',
            'goods','cbm',
            'ctns',
            'weight',
            'shipping_mark',
            'container_number',
            'remark',
        )
        widgets = {
           'client_name': forms.Select(attrs={
                'class':'form-control'
            }),
            'receipt_no': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'shipping_mark': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'cbm': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'goods': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'container_number': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'ctns': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'remark': forms.Textarea(attrs={
                'class':'form-control'
            }),
             'weight': forms.TextInput(attrs={
                'class':'form-control'
            }),
        }


# -------------------------------end of china ops -------------------------#






class CargoFormKenya(forms.ModelForm):
    class Meta:
        model = ReceivedCargoKenya
        fields = (
            'client_name','goods','cbm','ctns','weight','remark',
        )
        widgets = {
            'client_name': forms.Select(attrs={
                'class':'form-control'
            }),
            'goods': forms.Select(attrs={
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
            'remark': forms.Textarea(attrs={
                'class':'form-control'
            }),
            
        }

class dispatchFormKenya(forms.ModelForm):
    class Meta:
        model = DispatchCargoKenya
        fields=(
            'client_name',
            # 'receipt_no',
            'goods','cbm',
            'ctns',
            'weight',
            'remark',
            'delivery_number',
            'received_by',
            'Receiver_contact'
        )
        widgets = {
           'client_name': forms.Select(attrs={
                'class':'form-control'
            }),
            'cbm': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'goods': forms.Select(attrs={
                'class':'form-control'
            }),
            'delivery_number': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'ctns': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'remark': forms.Textarea(attrs={
                'class':'form-control'
            }),
             'weight': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'received_by': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'Receiver_contact': forms.TextInput(attrs={
                'class':'form-control'
            }),
            
        }


