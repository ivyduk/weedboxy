from django.shortcuts import render, redirect
from django.urls import reverse
from apps.users.forms import SubscribeForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db import IntegrityError 
from apps.products.models import Product
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from apps.users.forms import LoginForm
from apps.users.forms import UserRegistrationForm
from apps.users.forms import CustomPasswordResetForm
from apps.users.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm 
from .forms import UserEditForm, ProfileEditForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.tokens import default_token_generator


def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Su contraseña fue actualizada exitosamente!')
            return redirect('change_password_done')
        else:
            messages.error(request, 'Corrija el error a continuación.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'users/password_change_form.html', {
        'form': form
    })



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                email=cd['email'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'users/dashboard.html', {'form': form})
            else:
                form.add_error(None, "El correo y la contraseña no coinciden. Por favor, inténtalo de nuevo.")

                
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user
    context = {
        'user': user
    }

    return render(request,
                  'users/dashboard.html',
                  context )


def user_logout(request):
    
    logout(request)
    
    return render(request,
                  'users/logout.html',
                   )


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'users/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'users/register.html',
                  {'user_form': user_form})



def subscribe_home(request):  
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


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado con éxito')
        else:
            messages.error(request, '')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile)
    return render(request,
                  'users/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})



class CustomPasswordResetView(PasswordResetView):
    email_template_name = "users/password_reset_email.html"
    extra_email_context = None
    form_class = CustomPasswordResetForm
    from_email = None
    html_email_template_name = None
    success_url = reverse_lazy("password_reset_done")
    template_name = "users/password_reset_form.html"
    title = ("Password reset")
    token_generator = default_token_generator

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/password_reset_done.html"
    title = ("Password reset sent")
 