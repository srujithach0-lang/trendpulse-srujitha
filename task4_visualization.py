import pandas as pd
import matplotlib.pyplot as plt

def task_4_visualize(csv_input):
    df = pd.read_csv(csv_input)

    # Create a figure with 2 subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Plot 1. stories count by category
    df['category'].value_counts().plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_title("Stories collected per category")
    ax1.set_ylabel("count")

    # plot 2. Score vs num_comments scatter plot
    ax2.scatter(df['score'], df['num_comments'], alpha=0.5, color='green')
    ax2.set_title("upvotes vs. Engagement (comments)")
    ax2.set_xlabel("score")
    ax2.set_ylabel("Number of Comments")

    plt.tight_layout()
    plt.savefig("data/trend_analysis.png")
    print("Visualisation saved as data/trend_analysis.png")
    plt.show()

if __name__ == "__main__":
    task_4_visualize("data/trends_cleaned.csv")