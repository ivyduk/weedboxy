from django.contrib import admin

# Register your models here.

from .models import CultivationPlan
from .models import StagesCultivationPlan
from .models import PlanFeature

admin.site.register(CultivationPlan)
admin.site.register(StagesCultivationPlan)
admin.site.register(PlanFeature)