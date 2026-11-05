import matplotlib.pyplot as plt

def plot_dispersion(df):
    medianprops = {"color": "orange", "linewidth": 2}
    fig, (ax_box, ax,) = plt.subplots(1, 2, figsize=(9, 4), gridspec_kw={"width_ratios":{1,4}})
    ax_box.boxplot(df["revenue"], orientation="vertical", medianprops=medianprops)
    ax_box.set_title("Total Spridning")
    ax_box.grid(False)

    df.boxplot(column="revenue", by="category", ax=ax, medianprops=medianprops)
    fig.suptitle("Spridning")
    ax.set_title("Spridning per kategorier")
    ax.set_xlabel("")
    ax.grid(False)
    plt.tight_layout()
    
def plot_monthly_sales(monthly_sales):
    plt.figure(figsize=(9, 4))
    monthly_sales.plot(kind='line', marker='o', color='#2b5c8f', linewidth=2)
    plt.title('Monthly Sales Trend (När säljer vi?)')
    plt.xlabel('Month')
    plt.ylabel('Total Revenue (SEK)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

def plot_by_category(df):
    bar_colors = ['tab:cyan', 'tab:green', 'tab:blue', 'tab:purple', 'tab:orange', 'tab:red']
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.bar(df["category"], df["revenue"], color=bar_colors)
    ax.set_title("Intäkter per kategorier")
    ax.set_ylabel("Intäkter SEK")
    ax.grid(True, linestyle='dashed', axis="y")
    ax.ticklabel_format(style='plain', axis='y')
    plt.tight_layout()
    plt.show()

