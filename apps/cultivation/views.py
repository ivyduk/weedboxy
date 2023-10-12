from django.shortcuts import render
from .models import CultivationPlan
from apps.packages.models import Package

def cultivation_home(request):
    
    plans = CultivationPlan.objects.all()  
    
    return render(request, "cultivation/cultivation.html",  { 'plans': plans})

