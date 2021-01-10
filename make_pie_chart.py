import matplotlib.pyplot as plt

def make_pie_chart(artist_word_counts):

    labels = [pair[0] for pair in artist_word_counts]
    counts = [pair[1] for pair in artist_word_counts]
    explode = (0.1, 0, 0, 0, 0)

    figure, axis = plt.subplots()
    axis.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%')
    axis.axis('equal')
    plt.show()