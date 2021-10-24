import matplotlib.pyplot as plt
import matplotlib.animation as animation

from numpy import ndarray, arange, log10, logspace

class PlotTheSimulation():

    def __init__(self, mc:ndarray, prob:list, n_steps:int, figsize:(int, int) = (9, 6)):
        """

        :param mc:
        :param prob:
        :param n_steps:
        :param figsize:
        """

        self.mc = mc
        self.prob = prob

        self.n_steps = n_steps
        self.n_player = self.mc.shape[1]

        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.X_axis = arange(self.n_player)


    def setFiguer(self):
        """

        :return:
        """
        order = ["st", "nd", "rd"] + (["th"] * (self.n_player - 3))

        self.ax.grid(True, "major", axis="y", linestyle='-', linewidth=0.5, alpha=0.5, color="black")

        self.ax.set_xticks(self.X_axis)
        self.ax.set_xticklabels([str(i) + order[i - 1] for i in range(1, 1 + self.n_player)])

        self.ax.set_title(f"Probability of Crossing {self.n_steps}-steps Bridge \n for each Player's Order")
        self.ax.set_xlabel("Player Order")
        self.ax.set_ylabel("Probability")



    def plotFinalProb(self, i:int=-1):
        """

        :param i:
        :return:
        """
        self.ax.clear()
        self.setFiguer()
        self.ax.bar(self.X_axis - 0.2, self.mc[i], 0.4, label='Monte Carlo Probability')
        self.ax.bar(self.X_axis + 0.2, self.prob, 0.4, label='Calculated Probability')
        self.ax.text(0.2, 0.63, f"Iterration #{i}")
        self.ax.legend()

    def showPlot(self):
        self.plotFinalProb()

        self.fig.show()

    def savePlot(self):
        """

        :return:
        """
        self.plotFinalProb()
        self.fig.savefig(fname="plot.png")

    def saveAnimatedPlot(self, n_itter:int):
        """

        :param n_itter:
        :return:
        """
        itters = logspace(0, log10(n_itter-1), num=1000).astype(int)
        anim = animation.FuncAnimation(self.fig, self.plotFinalProb, frames = itters , interval=40 )

        anim.save(r'Animation.gif')