import matplotlib.pyplot as plt


def make_pie_chart(artist_word_counts):

    # get the labels
    labels = [pair[0] for pair in artist_word_counts]
    # get the counts
    counts = [pair[1] for pair in artist_word_counts]
    # break off the highest count
    # explode = (0.5, 0, 0, 0, 0)

    # make the chart
    figure, axis = plt.subplots()
    axis.pie(counts, shadow=True, labels=labels, autopct='%1.1f%%')
    axis.axis('equal')
    plt.tight_layout()
    plt.savefig(r"static/plot.png")

make_pie_chart([
    ("kanye", 65),
    ("taylor swift", 25),
    ("drake", 16),
    ("Ariana Grande", 8),
    ("Pink", 4),
])