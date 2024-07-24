from django.urls import path
from . import views

urlpatterns = [
    path('', views.employeeHome),
    path('profile/', views.profile, name='profile'),

]
