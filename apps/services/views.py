from django.shortcuts import render
from .forms import ServicesContactForm
from .models import Service
from .models import ServiceFeature
from django.contrib import messages
from apps.packages.models import Package
from apps.cultivation.models import CultivationPlan
from apps.cultivation.models  import StagesCultivationPlan
from apps.cultivation.models  import PlanFeature

def services_home(request):
    services = Service.objects.all()
    plans = CultivationPlan.objects.all()
    stagesplans = StagesCultivationPlan.objects.all()
    featuresplans = PlanFeature.objects.all()
    servicefeatures = ServiceFeature.objects.all()
    packages = Package.objects.filter(is_active=True).order_by('-created_at')[:3]
    service_choices = Service.objects.values_list('name', 'name').distinct()

    for package in packages:
        package.package_items

    if request.method == 'POST':
        form = ServicesContactForm(request.POST)
        if form.is_valid():
            form.save()     
            messages.success(request, '¡Tus datos han sido enviados satisfactoriamente, pronto nuestro equipo se pondrá en contacto contigo!')

        else: 
             messages.error(request, '¡Tus datos no se han podido guardar, intentalo de nuevo.')

    else:
        form = ServicesContactForm()

    
    context = {
        'form': form,
        'services': services,
        'packages': packages,
        'service_choices': service_choices,
        'plans': plans,
        'stagesplans': stagesplans,
        'featuresplans': featuresplans,
        'servicefeatures': servicefeatures,
    }

    return render(request, 'services/services.html', context)




