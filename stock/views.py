from django.shortcuts import render
from stock.models import Stock, CompanyData
import datetime
import csv
from django.contrib.auth.decorators import login_required

from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StockIndexSerializer, CompanyDataSerializer
from .models import Stock, CompanyData
from rest_framework.permissions import IsAuthenticated

class StockIndexView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        if(self.kwargs['indextype'] == "BSE"):
            queryset_filter = Stock.objects.filter(tag = 'Sensex').order_by('-id')
            queryset = queryset_filter[0]
            queryset_prev = queryset_filter[1]
            
        else:
            queryset_filter = Stock.objects.filter(tag = 'Nifty 50').order_by('-id')
            queryset = queryset_filter[0]
            queryset_prev = queryset_filter[1]

        serializer = StockIndexSerializer(queryset)
        store = returnMinAndHigh(queryset_filter)
        data = {
            'current' : serializer.data,
            'prev_close' : queryset_prev.close,
            'yearly_low' : store[1],
            'yearly_high' : store[0]
        }
        return Response(data)
    
class CompanyDataView(mixins.ListModelMixin, generics.GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = CompanyDataSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        company_name = self.kwargs['company_name']
        return CompanyData.objects.filter(company_name=company_name)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

def returnMinAndHigh(queryset_filter):
    curr_year = queryset_filter[0].date
    curr_year = int(curr_year.strftime('%Y'))
    i = 0
    yearly_lowest = queryset_filter[0].low
    yearly_highest = queryset_filter[0].high
    while(True):
        yearly_lowest = min(yearly_lowest, queryset_filter[i].low)
        yearly_highest = max(yearly_highest, queryset_filter[i].high)
        i += 1
        yearnow = queryset_filter[i].date
        yearnow = int(yearnow.strftime('%Y'))
        if(yearnow == curr_year - 1):
            break
    return [yearly_highest, yearly_lowest]

@login_required
def HomeView(request):
    return render(request, 'stock/master.html')



# Function to extract data from csv files and store in the database
# def scrapData(filename, name):
#     with open(filename) as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count != 0 and row[1] != 'null':
#                 split_date = row[0].split('-')
#                 d = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
#                 a = CompanyData(company_name = name, date = d, open_stock = float(row[1]), high = float(row[2]), low = float(row[3]), close = float(row[4]), adj_close = float(row[5]), volume = float(row[6]))
#                 a.save()
#             line_count += 1
#     print(f'Processed {line_count} lines.')
        
# scrapData('path_to_file', 'Type_of_Index/Company_Name')
