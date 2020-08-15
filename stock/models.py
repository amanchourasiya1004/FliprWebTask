from django.db import models

# Create your models here.
class Stock(models.Model):
    tag = models.CharField(max_length = 20, default='-')
    date = models.DateField(auto_now_add=False)
    open_stock = models.FloatField(default=0)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    close = models.FloatField(default=0)
    adj_close = models.FloatField(default=0)
    volume = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'StockIndex'
    
    def __str__(self):
        return str(self.date)

class CompanyData(models.Model):
    company_name = models.CharField(max_length = 30, default='-')
    date = models.DateField(auto_now_add=False)
    open_stock = models.FloatField(default=0)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    close = models.FloatField(default=0)
    adj_close = models.FloatField(default=0)
    volume = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'CompanyData'
    
    def __str__(self):
        return str(self.date)