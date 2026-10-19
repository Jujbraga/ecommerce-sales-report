
import csv

#https://docs.python.org/3/library/csv.html
with open("ecommerce-sales-report\\data\\ecommerce_sales.csv", newline="", encoding="utf-8" ) as f:
    reader = csv.reader(f)
    data = list(reader)