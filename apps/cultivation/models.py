from django.db import models
from apps.packages.models import Package
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


# Create your models here.

class CultivationPlan(Package):
    image = models.ImageField(upload_to='img/') 
    video = models.FileField(upload_to='videos/')    

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check if a CultivationPlan object already exists
        existing_plans = CultivationPlan.objects.all()

        # If an object already exists, delete it before saving the new one
        if existing_plans:
            for plan in existing_plans:
                plan.delete()

        # Call the original save method to save the object
        super(CultivationPlan, self).save(*args, **kwargs)


class StagesCultivationPlan(models.Model):
    step = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    name=models.CharField(max_length=100)
    cultivation_plan=models.ForeignKey(CultivationPlan, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.step)  
    
    def validate_unique(self, *args, **kwargs):
        # Verify that the step is unique for the specific cultivation_plan
        if self.cultivation_plan is not None:
            existing_steps = StagesCultivationPlan.objects.filter(
                cultivation_plan=self.cultivation_plan,
                step = self.step
                )         

            if existing_steps:
                raise ValidationError("The step must be unique to this cultivation plan.")

        super(StagesCultivationPlan, self).validate_unique(*args, **kwargs)