import matplotlib.pyplot as plt

def plot_monthly_sales(monthly_sales):
    """
    """
    plt.figure(figsize=(9, 4))
    monthly_sales.plot(kind='line', marker='o', color='#2b5c8f', linewidth=2)
    plt.title('Monthly Sales Trend (När säljer vi?)')
    plt.xlabel('Month')
    plt.ylabel('Total Revenue (SEK)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()