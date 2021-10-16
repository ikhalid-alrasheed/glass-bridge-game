import matplotlib.pyplot as plt
from numpy import array, arange

def plot_prob(mc:array, prob:list, i:int, save:bool=False) -> None:
    """

    :param mc:
    :param prob:
    :return:
    """
    order = ["st", "nd", "rd"] + (["th"] * (len(mc) - 3))
    X_axis = arange(len(mc))

    plt.figure(figsize=(12, 8))
    plt.bar(X_axis - 0.2, mc, 0.4, label='Monte Carlo')
    plt.bar(X_axis + 0.2, prob, 0.4, label='Probability')

    plt.xticks(X_axis, [str(i)+order[i-1] for i in range(1, 1+len(mc))])

    plt.xlabel("Player Order")
    plt.ylabel("Probability")
    plt.title(f"Probability of Passing {i}-steps Bridge \n for each Player Order")
    plt.legend()
    plt.show()
    if save:
        plt.savefig(fname="plot.png")

