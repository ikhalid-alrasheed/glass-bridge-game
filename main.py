from game_probability import get_prob_live
from game import GlassBridgeGame
from plotting import PlotTheSimulation

if __name__ == '__main__':
    players = 16
    steps = 18
    itters = 100000

    game = GlassBridgeGame(players, steps)
    mc = game.mc_simulation(itters)

    prob = [round(get_prob_live(i, steps), 4) for i in range(1, players+1)]

    plot = PlotTheSimulation(mc, prob, steps)
    plot.saveAnimatedPlot(itters)
