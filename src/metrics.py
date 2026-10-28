import csv
from src import io_utils as io  


def unique_list_of_category(data, category):
    list_of_category = list(set(row[category] for row in data[1:]))
    return list_of_category
list_of_cities = unique_list_of_category(io.data, 2)
list_of_products = unique_list_of_category(io.data, 3)

def total_revenue(data):
    revenue = 0
    for value in range(len(data) -1):
        revenue += float(data[value + 1][4])
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
            revenue += float(data[value + 1][4])
    return revenue
def revenue_for_products(data, list_of_products):
    revenues = []
    for product in list_of_products:
        revenues.append([product,(revenue_for_product(data, product))])
    return revenues

def revenue_for_city(data, city):
    revenue = 0
    for value in range(len(data) -1):
        if data[value + 1][2] == city:
           revenue += float(data[value + 1][4])
    return revenue

def revenue_for_cities(data, list_of_cities):
    revenues = []
    for city in list_of_cities:

        revenues.append([city,(revenue_for_city(data, city))])
    return revenues

def avrage_order_value(data):
    revenue = total_revenue(data)
    return revenue / (len(data)-1)


def sorted_revenue_for_products(data, list_of_products):
    sorted_data = sorted(revenue_for_products(data, list_of_products), key=lambda x: float(x[1]), reverse=True)
    return sorted_data


if __name__ == "__main__":
    print("Revenue for products:")
    print(revenue_for_products(io.data, list_of_products))
    print("Sorted revenue for products:")
    print(sorted_revenue_for_products(io.data, list_of_products))
    print("Revenue for cities:")
    print(revenue_for_cities(io.data, list_of_cities))
    print("Total revenue:")
    print(total_revenue(io.data))
    print("Total units sold:")
    print(total_units_sold(io.data))
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