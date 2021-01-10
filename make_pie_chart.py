import matplotlib.pyplot as plt


def make_pie_chart(artist_word_counts):

    # get the labels
    labels = [artist_word_counts["Artist"] for _ in artist_word_counts]
    # get the counts
    counts = [artist_word_counts['Lyrics count'] for _ in artist_word_counts]
    # break off the highest count
    # explode = (0.5, 0, 0, 0, 0)

    # make the chart
    figure, axis = plt.subplots()
    axis.pie(counts, shadow=True, labels=labels, autopct='%1.1f%%')
    axis.axis('equal')
    plt.tight_layout()
    plt.savefig(r"static/plot.png")

