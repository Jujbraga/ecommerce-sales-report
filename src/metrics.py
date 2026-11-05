import pandas as pd

def top3(df):

    df = pd.read_csv('ecommerce_sales.csv')

    cat = df.groupby("category")["revenue"].sum().sort_values(ascending=False).head(3)

#print(cat)
    print("The top 3 categories by revenue are:\n", cat)
    return cat