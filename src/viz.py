import matplotlib.pyplot as plt

def plot_aov(df):
    fig, ax = plt.subplots()
    ax.scatter(df["date"], df["revenue"], alpha=0.6)
    ax.set_title("Revenue vs date")
    ax.set_xlabel("date")
    ax.set_ylabel("Revenue")
    plt.tight_layout()