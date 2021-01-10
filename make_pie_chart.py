import matplotlib.pyplot as plt
from artist_used_most import artist_used_most, open_file

wc = artist_used_most("hello", open_file())


def make_pie_chart(artist_counts):

    # get the labels
    labels = [
        artist_counts[num]["Artist"] + " - " + str(artist_counts[num]['Lyrics count'])
        for num in range(len(artist_counts))
    ]
    # get the counts
    counts = [artist_counts[num]['Lyrics count'] for num in range(len(artist_counts))]
    # break off the highest count
    # explode = (0.5, 0, 0, 0, 0)

    # make the chart
    figure, axis = plt.subplots()
    axis.pie(counts, labels=labels, autopct='%1.1f%%')
    axis.axis('equal')
    plt.tight_layout()
    plt.savefig(r"static/plot.png")

make_pie_chart(wc)
