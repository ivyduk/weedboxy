from django.urls import path
from . import views


urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses_home'),
    path('subject/<slug:subject>/',views.CourseListView.as_view(),name='course_list_subject'),
    path('<slug:slug>/',views.CourseDetailView.as_view(),name='course_detail'),

]