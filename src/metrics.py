import csv
import sys, os

sys.path.append(os.path.abspath(".."))

import src.io_utils as io  

import pandas as pd

def by_category(df):
    return (
        df.groupby("category", dropna=False)["revenue"].sum()
        .sort_values(ascending=False)
        .reset_index()
    )

def show_avg(df):
    avg =df.agg(
        mean = ("revenue", "mean"),
        median = ("revenue", "median"),
        std = ("revenue", "std"),
        max = ("revenue", "max"),
        min = ("revenue", "min"),
    ).round(2)
    return avg

def top3(df):
    cat = df.groupby("category")["revenue"].sum().sort_values(ascending=False).head(3)
    return cat

def unique_list_of_category(data, category):
    list_of_category = list(set(row[category] for row in data[1:]))
    return list_of_category
list_of_cities = unique_list_of_category(io.data, 2)
list_of_categories = unique_list_of_category(io.data, 3)

def total_revenue(data):
    revenue = 0
    for value in range(len(data) -1):
        revenue += float(data[value + 1][6])
    return revenue


def total_units_sold(data):
    units_sold = 0
    for value in range(len(data) -1):
        units_sold += int(data[value + 1][5])
    return units_sold

def revenue_for_product(data, product):
    revenue = 0
    for value in range(len(data)-1):
        if data[value + 1][3] == product:
            revenue += float(data[value + 1][6])
    return revenue
def revenue_for_products(data, list_of_categories):
    revenues = []
    for product in list_of_categories:
        revenues.append([product,(revenue_for_product(data, product))])
    return revenues

def revenue_for_city(data, city):
    revenue = 0
    for value in range(len(data) -1):
        if data[value + 1][2] == city:
           revenue += float(data[value + 1][6])
    return revenue

def revenue_for_cities(data, list_of_cities):
    revenues = []
    for city in list_of_cities:

        revenues.append([city,(revenue_for_city(data, city))])
    return revenues

def average_order_value(data):
    revenue = total_revenue(data)
    return revenue / (len(data)-1)


def sorted_revenue_by_category(data, list_of_categories):
    sorted_data = sorted(revenue_for_products(data, list_of_categories), key=lambda x: float(x[1]), reverse=True)
    return sorted_data

# Nyckeltal
total_revenue_sold = round(total_revenue(io.data), 2)
total_units = total_units_sold(io.data) #ok
aov = average_order_value(io.data) #ok
revenue_category = sorted_revenue_by_category(io.data, list_of_categories) #ok
revenue_city = revenue_for_cities(io.data, list_of_cities)
# top_3 = 


def sorted_revenue_for_cities(data, list_of_cities):
    sorted_data = sorted(revenue_for_cities(data, list_of_cities), key=lambda x: float(x[1]), reverse=True)
    return sorted_data


def calculate_revenue_by_category(sales_data):
    category_index = 3
    revenue_index = 6
    category_revenue = {}
    
    for row in sales_data[1:]:
        category = row[category_index]
        revenue = float(row[revenue_index])
        if category in category_revenue:
            category_revenue[category] += revenue
        else:
            category_revenue[category] = revenue
            
    return category_revenue

if __name__ == "__main__":
    print("Revenue for category:")
    print(revenue_category)
    print("Sorted revenue for category:")
    print(revenue_category)
    print("Revenue for cities:")
    print(revenue_city)
    print("Total revenue:")
    print(total_revenue_sold)
    print("Total units sold:")
    print(total_units)
    print("Average order value:")
    print(avrage_order_value(io.data))
    import pandas as pd

def get_monthly_sales_analysis(df):
    """

    """
    df['date'] = pd.to_datetime(df['date'])
    df['revenue'] = pd.to_numeric(df['revenue'])
    
    monthly_sales = df.groupby(df['date'].dt.to_period('M'))['revenue'].sum()
    return monthly_sales
def calculate_revenue_by_city(sales_data):
    city_index = 2
    revenue_index = 6
    city_revenue = {}
    
    for row in sales_data[1:]:
        city = row[city_index]
        revenue = float(row[revenue_index])
        if city in city_revenue:
            city_revenue[city] += revenue
        else:
            city_revenue[city] = revenue
            
    return city_revenue

def calculate_revenue_by_category(sales_data):
    category_index = 3
    revenue_index = 6
    category_revenue = {}
    
    for row in sales_data[1:]:
        category = row[category_index]
        revenue = float(row[revenue_index])
        if category in category_revenue:
            category_revenue[category] += revenue
        else:
            category_revenue[category] = revenue
            
    return category_revenue

def calculate_total_revenue(sales_data):
    revenue_index = 6
    total_revenue = 0
    
    for row in sales_data[1:]:
        total_revenue += float(row[revenue_index])
        
    return total_revenue
