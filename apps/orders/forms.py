from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 
                  'postal_code', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': ' Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': ' Apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'address': forms.TextInput(attrs={'placeholder': 'Dirección'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Código Postal'}),
            'city': forms.TextInput(attrs={'placeholder': 'Ciudad'}),
        }