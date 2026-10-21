import csv
import io_utils as io  


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
    print(aov)