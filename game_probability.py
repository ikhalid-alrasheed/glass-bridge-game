
from math import comb


def get_prob_live(player_order, steps):
    prob_die = 0
    for k in range(player_order, steps + 1):
        prob_die += comb(k - 1, player_order - 1) * (1 / 2) ** k

    return 1 - prob_die
