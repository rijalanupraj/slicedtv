# External Import
from django.urls import path

# Internal Import
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
]
