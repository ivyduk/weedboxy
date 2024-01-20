import re
from django import forms
from .models import ServicesContact
from apps.services.models import Service

class ServicesContactForm(forms.ModelForm):
    class Meta:
    
        services = forms.ModelChoiceField(
            queryset=Service.objects.all(), 
            
        )

    class Meta:
        model = ServicesContact
        fields = ['first_name', 'last_name', 'phone', 'email', 'services']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': ' Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': ' Apellido'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name)>100:
            raise forms.ValidationError('El nombre es demasiado largo.')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name)>100:
            raise forms.ValidationError('El apellido es demasiado largo.')
        return last_name
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone_regex = r'^\d{7,15}$'  
        if not re.match(phone_regex, phone):
            raise forms.ValidationError('El número de teléfono no tiene un formato válido.')
        return phone
