from django.urls import path
from . import views

urlpatterns = [
    path('shrek/', views.say_shrek)
]