
class Player:
    VERSION = "2.0"

    def betRequest(self, game_state):


        # first orbit -> not valid
            # suited
            # paired
            # connectors
            # face card/ace
        print("=================================")
        print(game_state)
        print("orbits    %d" % game_state['orbits'])
        print("round     {:d}".format(game_state['round']))
        print("bet_index %d" % game_state['bet_index'])
        return game_state['current_buy_in'] - game_state['players'][game_state["in_action"]]["bet"]

    def showdown(self, game_state):
        print("=================================")
        print(game_state)
        print("=================================")

    # TODO: is "orbit" correct
    # def is_first_orbit(self, game_state):
    #     return game_state['orbits'] == 0

