
class Player:
    VERSION = "1.0"

    def betRequest(self, game_state):
        return game_state['current_buy_in'] - game_state['players'][game_state["in_action"]]["bet"]

    def showdown(self, game_state):
        pass

