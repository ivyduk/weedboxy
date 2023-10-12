from django import forms
from apps.users.models import UserAccount

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['email']  

    def clean(self):
        data = self.cleaned_data

        already_subscribed = UserAccount.objects.filter(email=data.get('email_subscribe')).first()

        
        if already_subscribed and already_subscribed.is_subscribed:
            self.add_error('email_subscribe', 'Correo electrónico ya se encuentra suscrito.')

        
        return data