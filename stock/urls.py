from django.urls import path
from .views import StockIndexView, HomeView, CompanyDataView

urlpatterns = [
    path('stock/index/<indextype>/', StockIndexView.as_view(), name = 'StockIndexView'),
    path('api/company_data/<company_name>/', CompanyDataView.as_view(), name = 'CompanyDataView'),
    path('home/', HomeView, name = 'HomeView'),
]