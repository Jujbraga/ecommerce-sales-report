import pandas as pd

class EcommerceAnalyzer:
    def __init__(self, df):
        self.df = df

    def calculate_avg(self):
        avg = self.df.agg(
            mean = ("revenue", "mean"),
            median = ("revenue", "median"),
            std = ("revenue", "std"),
            max = ("revenue", "max"),
            min = ("revenue", "min")
        ).round(2)
        return avg