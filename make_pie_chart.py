import matplotlib.pyplot as plt
from artist_used_most import artist_used_most, open_file
from PIL import Image

wc = artist_used_most("hello", open_file())


def make_pie_chart(artist_counts):

    # get the labels
    labels = [
        f"{artist_counts[num]['Artist']} ({str(artist_counts[num]['Lyrics count'])})"
        for num in range(len(artist_counts))
    ]
    # get the counts
    counts = [artist_counts[num]['Lyrics count'] for num in range(len(artist_counts))]
    # break off the highest count
    # explode = (0.5, 0, 0, 0, 0)

    # make the chart
    if sum(counts) > 0:
        figure, axis = plt.subplots()
        axis.pie(counts, labels=labels, autopct='%1.1f%%', normalize=True)
        axis.axis('equal')
        plt.rc('font', family='Franklin Gothic Book')
        plt.title('Which artist used the word the most?')
        plt.tight_layout()
        plt.savefig(r"static/plot.png")
        plot_img = Image.open(r"static/plot.png")
        plot_img = plot_img.resize((750, 550))
        plot_img.save(r"static/plot.png", 'PNG')
    else:
        image = Image.open(r"./static/no_results_found.png")
        image = image.resize((640, 480))
        image.save(r"./static/plot.png", 'PNG')


make_pie_chart(wc)
