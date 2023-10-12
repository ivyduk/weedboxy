from django.shortcuts import render
from django.urls import reverse
from apps.users.forms import SubscribeForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db import IntegrityError 
from apps.products.models import Product
from config.cart import Cart



def index(request):  

   
    products = Product.objects.all()[:4]
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            
            try:
                user_account = form.save(commit=False)
                user_account.is_subscribed = True  
                user_account.save()
                messages.success(request, '¡Tus datos han sido enviados satisfactoriamente, pronto nuestro equipo se pondrá en contacto contigo!')
                return HttpResponseRedirect(reverse('index'))
            
            except IntegrityError:
                messages.error(request, 'El correo electrónico ya está registrado.')
    else:
        form = SubscribeForm()

    return render(request, 'index.html', {'form': form, 'products': products })



def about_home(request):
    return render(request, "about/about.html")