from django.urls import path
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('', RegisterView.as_view(), name = 'RegisterView'),
    path('accounts/login/', LoginView, name = 'LoginView'),
    path('accounts/logout/', LogoutView, name = 'LogoutView'),
]