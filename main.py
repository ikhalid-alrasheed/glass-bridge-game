from game_probability import get_prob_live
from game import GlassBridgeGame
from plotting import plot_prob

if __name__ == '__main__':
    players = 16
    steps = 18
    game = GlassBridgeGame(players, steps)
    mc = game.mc_simulation(1000000)

    prob = [round(get_prob_live(i, steps), 4) for i in range(1, players+1) ]

    plot_prob(mc, prob, steps, True)
