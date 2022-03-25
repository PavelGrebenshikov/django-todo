from django.urls import path, include
from django.contrib.auth import views
from .views import RegisterView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', RegisterView.as_view(), name='registration'),
]