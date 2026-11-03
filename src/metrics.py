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