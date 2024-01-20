from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class ModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class PricingMixin(models.Model):
    
    class PricingType(models.TextChoices):
        FIXED = "FIXED", _("Fixed")
        DAILY = "DAYLY", _("Daily")
        WEEKLY = "WEEKLY", _("Weekly")
        MONTLY = "MONTHLY", _("Monthly")
        YEARLY = "YEARLY", _("Yearly")

    pricing_type = models.CharField(
        max_length=7,
        choices=PricingType.choices,
        default=PricingType.FIXED,
    )
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)], default=0)

    
    class Meta:
        abstract = True

    
    @property
    def discounted_price(self):
        return ((self.price)*(self.discount_percentage))/100 
    
    @property
    def total_price(self):
        return self.price - self.discounted_price if self.has_discount else self.price
    
    @property
    def has_discount(self):
        return self.discount_percentage > 0