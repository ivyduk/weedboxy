from django.shortcuts import render, get_object_or_404
from .models import Course
from django.urls import reverse_lazy
from django.db.models import Count
from .models import Subject
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.detail import DetailView
from apps.courses.models import Module
from apps.courses.models import Course 



class CourseListView(TemplateResponseMixin, View):
    model = Course
    template_name = 'courses/courses.html'

    def get(self, request, subject=None):
        subjects = Subject.objects.annotate(total_courses=Count('courses'))
        courses = Course.objects.annotate(total_modules=Count('modules'))
        modules = Module.objects.all()

        if subject:
            subject = get_object_or_404(Subject, slug=subject)
            courses = courses.filter(subject=subject)
            modules = modules.all()
        return self.render_to_response({'subjects': subjects,'subject': subject,'courses': courses, 'modules': modules})
    

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course/detail.html'
    
        
        

    

