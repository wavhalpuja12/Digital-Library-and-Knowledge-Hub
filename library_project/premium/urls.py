from django.urls import path
from . import views

urlpatterns = [
    path('upgrade/', views.upgrade_premium, name='upgrade_premium'),
    path('activate/', views.activate_premium, name='activate_premium'),
    path('members/', views.premium_members, name='premium_members'),
]
