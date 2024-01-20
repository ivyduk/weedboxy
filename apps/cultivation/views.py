from django.shortcuts import render
from .models import CultivationPlan
from .models import StagesCultivationPlan
from .models import PlanFeature

def cultivation_home(request):
    
    plans = CultivationPlan.objects.all()   
    stagesplans = StagesCultivationPlan.objects.all()  
    featuresplans = PlanFeature.objects.all()



    
    return render(request, "cultivation/cultivation.html",  { 'plans': plans, 'stagesplans': stagesplans, 'featuresplans': featuresplans})

