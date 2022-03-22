import matplotlib.pyplot as plt

def display(x, y1, y2, fn):
    """
    Résumé de la fonction
    :param x: toto
    :param y1: titi
    :param y2: tutu
    :return:
    """
    # plt.subplot(211)
    plt.plot(x, fn(x), color="red")
    plt.scatter(x, y1)
    # plt.subplot(212)
    # plt.scatter(x, y2)
    plt.show()