from django.shortcuts import render
from stock.models import Stock, CompanyData
import datetime
import csv


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
        
# scrapData('path_to_file', 'Type of Index/Company')
