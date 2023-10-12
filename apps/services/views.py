from django.shortcuts import render
from .forms import ServicesContactForm
from .models import Service
from django.contrib import messages
from apps.packages.models import Package

def services_home(request):
    services = Service.objects.all()  
    
    packages = Package.objects.filter(is_active=True).order_by('-created_at')[:3]

    service_choices = Service.objects.values_list('name', 'name').distinct()

    for package in packages:
        package.package_items

    if request.method == 'POST':
        form = ServicesContactForm(request.POST)
        if form.is_valid():
            form.save()     
            messages.success(request, '¡Tus datos han sido enviados satisfactoriamente, pronto nuestro equipo se pondrá en contacto contigo!')
            return render(request, 'services/services.html', {'form': ServicesContactForm(request.GET), 'services': services, 'packages': packages,  'service_choices': service_choices})
    else:
        form = ServicesContactForm()

    

    
    return render(request, "services/services.html",  {'form': form, 'services': services, 'packages': packages,  'service_choices': service_choices})



