import re
from django import forms
from apps.users.models import UserAccount
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from apps.users.models import Profile
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from datetime import date


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['email']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Ingresa tu correo electrónico'}),
        }

    def clean(self):
        data = self.cleaned_data

        already_subscribed = UserAccount.objects.filter(email=data.get('email_subscribe')).first()

        if already_subscribed and already_subscribed.is_subscribed:
            self.add_error('email_subscribe', 'Correo electrónico ya se encuentra suscrito.')

        return data
    

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Correo electronico'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Repite la contraseña'}))

    date_of_birth = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'placeholder': 'Fecha de nacimiento'}),
        label='Date of Birth',
        
    )


    class Meta:
        model = UserAccount
        fields = [ 'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth' ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': ' Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': ' Apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Teléfono'}),
            
        }


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']
    
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
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        phone_regex = r'^\d{7,15}$'  
        if not re.match(phone_regex, phone_number):
            raise forms.ValidationError('El número de teléfono no tiene un formato válido.')
        return phone_number

    def clean_email(self):
        data = self.cleaned_data['email']
        if UserAccount.objects.filter(email=data).exists():
            raise forms.ValidationError('Este email ya se encuentra en uso.')
        return data
    
    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        if dob:
            age = date.today().year - dob.year - ((date.today().month, date.today().day) < (dob.month, dob.day))
            if age < 18:
                raise forms.ValidationError("Debes ser mayor de 18 años para registrarte.")
        return dob



class CustomPasswordChangeForm(PasswordChangeForm):
      
    error_messages = {
        "password_mismatch": ("Las dos contraseñas no coinciden."),
        
        "password_incorrect": (
            "Su antigua contraseña es incorrecta. Por favor ingrésela nuevamente." ),                 
    }
    old_password = forms.CharField(
        label="Contraseña actual", widget=forms.PasswordInput(attrs={'autocomplete': 'off','data-toggle': 'password', 'type' : 'password', 'class': ' input form-control' }))
        
    
    new_password1 = forms.CharField(
        label="Nueva contraseña", widget=forms.PasswordInput(attrs={'autocomplete': 'off','data-toggle': 'password'}))
      
    
    new_password2 = forms.CharField(
        label="Confirmar nueva contraseña", widget=forms.PasswordInput(attrs={'autocomplete': 'off','data-toggle': 'password'}))
        
    

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']
    

class UserEditForm(forms.ModelForm):
    class Meta:
        phone_number = forms.CharField(max_length=15, required=True, label='Teléfono')
        model = UserAccount
        fields = ['first_name', 'last_name', 'phone_number', 'email']

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
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        phone_regex = r'^\d{7,15}$'  
        if not re.match(phone_regex, phone_number):
            raise forms.ValidationError('El número de teléfono no tiene un formato válido.')
        return phone_number

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = UserAccount.objects.exclude(id=self.instance.id)\
                         .filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Este email ya se encuentra en uso.')
        return data


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label= ("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

