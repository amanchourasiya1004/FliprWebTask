from django.contrib import admin
from .models import Stock, CompanyData

# Register your models here.
admin.site.register(Stock)
admin.site.register(CompanyData)
