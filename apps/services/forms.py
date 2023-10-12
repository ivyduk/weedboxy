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