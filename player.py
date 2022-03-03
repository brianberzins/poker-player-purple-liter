from collections import Counter
import numpy

class Player:
    VERSION = "3.3"

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

        print("hole cards:")
        print("    %s" % self.my_cards(game_state)[0])
        print("    %s" % self.my_cards(game_state)[0])

        print("community cards:")
        for card in self.community_cards(game_state):
            print("    %s" % card)

        if self.should_fold(game_state):
            print("folding")
            return 0

        print("calling")
        return game_state['current_buy_in'] - game_state['players'][game_state["in_action"]]["bet"]

    def showdown(self, game_state):
        print("=================================")
        print(game_state)
        print("=================================")

    def has_face_card(self, cards):
        for card in cards:
            if card['rank'] in ['A', 'K', 'Q', 'J']:
                return True
        return False

    def has_pair_hole_cards(self, cards):
        return cards[0]['rank'] == cards[1]['rank']

    def my_cards(self, game_state):
        return game_state['players'][game_state["in_action"]]["hole_cards"]

    def community_cards(self, game_state):
        return game_state['community_cards']

    def should_fold(self, game_state):
        cards = self.my_cards(game_state)
        return not (self.has_face_card(cards) or self.has_pair_hole_cards(cards))

    def get_cards(self, game_state):
        cards = self.my_cards(game_state)
        cards.extend(self.community_cards(game_state))
        return cards

    def should_raise(self, cards):
        ranks = list(map(lambda c: c['rank'], cards))
        counter = Counter(ranks)
        return max(counter.values()) >= 3
