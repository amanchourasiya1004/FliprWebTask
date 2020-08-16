from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('', RegisterView.as_view(), name = 'RegisterView'),
    path('accounts/login/', LoginView, name = 'LoginView'),
]