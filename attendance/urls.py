from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_attendance/', views.add_attendance, name='add_attendance'),
    path('attendance_list/', views.attendance_list, name='attendance_list'),
    path('student_list/', views.student_list, name='student_list'),
    path('course_list/', views.course_list, name='course_list'),
]