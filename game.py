from numpy import array, random, append, ndarray


class GlassBridgeGame():

    def __init__(self, n_players: int, n_steps: int):
        """
        :param n_players: number of players
        :param n_steps: number of the bridge's steps (how long is the bridge?)
        """
        self.n_players = n_players
        self.n_steps = n_steps
        self.bridge_odds = [0.5] * self.n_steps

    def onePlayerRound(self) -> bool:
        """
        An attempt for a player to walk over the bridge
            and evaluate if he had a successful endeavor or not
        This method will modify the steps probability every time it runs.

        :return: Bool ( True if he crossed the bridge)
        """
        if self.bridge_odds[-1] == 1 :
            return True

        for order, odd_of_pass in enumerate(self.bridge_odds):
            if odd_of_pass < 1:
                self.bridge_odds[order] = 1
                if random.rand() > odd_of_pass:
                    break
                else:
                    # if it is the last step
                    if order == (self.n_steps - 1):
                        return True
        return False

    def oneFullRound(self) -> ndarray:
        """

        :return:
        """
        output = []
        for player in range(self.n_players):
            output.append(self.onePlayerRound())

        return array(output).astype(int)

    def mc_simulation(self, n_runs: int) -> ndarray:
        """

        :param n_runs:
        :return:
        """
        self.resetBridge()
        crossing_counter: ndarray = self.oneFullRound()
        odds = array([crossing_counter / 1])
        for run in range(1, n_runs):
            self.resetBridge()
            crossing_counter += self.oneFullRound()
            odds = append(odds , [crossing_counter / (run+1)], axis=0)

        return odds

    def resetBridge(self):
        """
        reset the steps probability to 0.5 for every step
        :return: None
        """
        self.bridge_odds = [0.5] * self.n_steps
