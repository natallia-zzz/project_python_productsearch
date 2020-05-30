# transfer script
csv_filepathname="/Users/natalliazzz/downloads/github/project_python_productsearch/productsite/amazon.csv"
your_djangoproject_home="/Users/natalliazzz/downloads/github/project_python_productsearch/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] ='productsite.settings'

from products.models import Product

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"', encoding = 'utf-16')

from decimal import Decimal

for row in dataReader:
    product = Product()
    product.pr_id=row[0]
    product.pr_title=row[1]
    try:
        product.pr_description=row[2]
    except UnicodeDecodeError:
        pass
    product.pr_manufacturer=row[3]
    product.pr_price=row[4]
    product.save()

import pandas as pd                                                                                                   

data=pd.read_csv(csv_filepathname, encoding='latin')          
for row in data:
    product = Product()
    product.pr_id=row[0]
    product.pr_title=row[1]
    try:
        product.pr_description=row[2]
    except UnicodeDecodeError:
        pass
    product.pr_manufacturer=row[3]
    product.pr_price=row[4]
    product.save()

