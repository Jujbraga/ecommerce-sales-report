from io_utils import df
import pandas as pd

avg = df.agg(
    mean = ("revenue", "mean"),
    median = ("revenue", "median"),
    std = ("revenue", "std"),
    max = ("revenue", "max"),
    min = ("revenue", "min"),
)
print(avg)


def calculate_revenue(data):
    data = list(data)
    revenue = 0
    for value in data:
        revenue += float(value)
    return round(revenue, 2)

unique_order = set(df["order_id"])


def calculate_aov(total, units):
    aov = total / units
    aov_formatted = f"{aov:_.2f} kr".replace('.', ',').replace('_', ' ')
    return aov_formatted


total_revenue = calculate_revenue(df["revenue"])
total_units_sold = df["units"].count()
# aov = df["revenue"].mean()
aov = calculate_aov(total_revenue, total_units_sold)

print(total_units_sold)
print(aov)