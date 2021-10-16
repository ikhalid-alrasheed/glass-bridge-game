from game_probability import get_prob_live
from game import GlassBridgeGame
from plotting import plot_prob

if __name__ == '__main__':
    game = GlassBridgeGame(16, 18)
    mc = game.mc_simulation(1000000)

    prob = [round(get_prob_live(i, 18), 4) for i in range(1, 17) ]

    plot_prob(mc, prob, 18, True)
