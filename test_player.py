import player
import json

# def test_bet_before():
#     subject = player.Player()
#     game_stats = json.load(open('example_should_fold.json'))
#     assert subject.has_bet_before(game_stats)

# def test_first_round_true():
#     subject = player.Player()
#     game_stats = json.load(open('example_should_fold.json'))
#     assert subject.is_first_orbit(game_stats)
#
# def test_first_orbit_false():
#     subject = player.Player()
#     game_stats = json.load(open('example_call.json'))
#     assert not subject.is_first_orbit(game_stats)

def test_should_fold():
    subject = player.Player()
    game_state = json.load(open('example_should_fold.json'))
    assert subject.should_fold(game_state)

def test_not_fold_because_pairs():
    subject = player.Player()
    game_state = json.load(open('example_with_pair.json'))
    assert not subject.should_fold(game_state)

def test_should_not_fold_because_face_cards():
    subject = player.Player()
    game_state = json.load(open('example_call.json'))
    assert not subject.should_fold(game_state)


def test_call():
    subject = player.Player()
    game_stats = json.load(open('example_call.json'))
    assert 240 == subject.betRequest(game_stats)

# def test_bet_first_round():
#     subject = player.Player()
#     game_stats = json.load(open('example_should_fold.json'))
#     assert 480 == subject.betRequest(game_stats)