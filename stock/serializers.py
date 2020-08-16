from rest_framework import serializers
from .models import Stock, CompanyData


class StockIndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ('tag', 'date', 'high', 'open_stock', 'low', 'close', 'adj_close', 'volume')

class CompanyDataSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = CompanyData
        fields = ('date', 'close')
