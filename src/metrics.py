import sys, os

sys.path.append(os.path.abspath(".."))

import src.io_utils as io  
import pandas as pd

def print_summary(list, title):
    title = title
    print(title)
    for category, total in list:
        print(f"{category}: {total:,.2f} SEK")


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

def calculate_drop_increase(previous, current):
    result = (current - previous) / previous
    if result < 0:
        return (f"Minskning av intäkter under perioden: {result:.2%}")
    if result > 0:
        return (f"Ökning av intäkter under perioden: {result:.2%}")

def unique_list_of_category(data, category):
    list_of_category = list(set(row[category] for row in data[1:]))
    return list_of_category
list_of_cities = unique_list_of_category(io.data, 2)
list_of_categories = unique_list_of_category(io.data, 3)


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

def sorted_revenue_by_category(data, list_of_categories):
    sorted_data = sorted(revenue_for_products(data, list_of_categories), key=lambda x: float(x[1]), reverse=True)
    return sorted_data

def sorted_revenue_for_cities(data, list_of_cities):
    sorted_data = sorted(revenue_for_cities(data, list_of_cities), key=lambda x: float(x[1]), reverse=True)
    return sorted_data

def get_monthly_sales_analysis(df):
    df['date'] = pd.to_datetime(df['date'])
    df['revenue'] = pd.to_numeric(df['revenue'])
    
    monthly_sales = df.groupby(df['date'].dt.to_period('M'))['revenue'].sum()
    return monthly_sales
