from collections import Counter

class Player:
    VERSION = "5.0"

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
        for card in self.my_cards(game_state):
            print("    %s" % card)

        print("community cards:")
        for card in self.community_cards(game_state):
            print("    %s" % card)

        if self.should_fold(game_state):
            print("folding")
            return 0
        to_call = self.to_call(game_state)
        if to_call > self.current_bet(game_state) * 2:
            print(to_call)
            print(self.current_bet(game_state) * 2)
            print("too risky - folding")
            return 0 # fold
        cards = self.get_cards(game_state)
        if self.should_raise(cards):
            print("raising")
            return self.to_call(game_state) + game_state["minimum_raise"]
        print("calling")
        return self.to_call(game_state)

    def to_call(self, game_state):
        return game_state['current_buy_in'] - self.current_bet(game_state)

    def current_bet(self, game_state):
        return game_state['players'][game_state["in_action"]]["bet"]

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
        card_map = map(lambda c: c['rank'], cards)
        ranks = list(card_map)
        print(cards)
        print(ranks)
        counter = Counter(ranks)
        return max(counter.values()) >= 3
