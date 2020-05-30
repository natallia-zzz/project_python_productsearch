# transfer script
csv_filepathname="/Users/natalliazzz/downloads/github/project_python_productsearch/productsite/amazon.csv"
your_djangoproject_home="/Users/natalliazzz/downloads/github/project_python_productsearch/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] ='productsite.settings'

from products.models import Product

import csv
dataReader = csv.reader(open(csv_filepathname, encoding = 'latin_1'), delimiter=',', quotechar='"')
from decimal import Decimal

for row in dataReader:
    product = Product()
    product.pr_id=row[0]
    product.pr_title=row[1]
    product.pr_description=row[2]
    product.pr_manufacturer=row[3]
    product.pr_price=row[4]
    product.save()
