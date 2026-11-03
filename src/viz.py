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