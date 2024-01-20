from django.db import models
from django.contrib.auth import get_user_model 
from apps.orders.models import SKUItem
from config.mixins import ModelMixin
from apps.packages.models import PackageItem




class Subject(ModelMixin):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title
    

class Course(PackageItem):
    owner = models.ForeignKey(get_user_model(),
                related_name='courses_created',
                on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,
                related_name='courses',
                on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.name


class Module(ModelMixin):
    course = models.ForeignKey(Course,
                        related_name='modules',
                        on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
 
    def __str__(self):
        return self.title
