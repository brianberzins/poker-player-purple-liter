import player
import json

# def test_bet_before():
#     subject = player.Player()
#     game_stats = json.load(open('example_bet_first_round.json'))
#     assert subject.has_bet_before(game_stats)

# def test_first_round_true():
#     subject = player.Player()
#     game_stats = json.load(open('example_bet_first_round.json'))
#     assert subject.is_first_orbit(game_stats)
#
# def test_first_orbit_false():
#     subject = player.Player()
#     game_stats = json.load(open('example_call.json'))
#     assert not subject.is_first_orbit(game_stats)

def test_call():
    subject = player.Player()
    game_stats = json.load(open('example_call.json'))
    assert 240 == subject.betRequest(game_stats)