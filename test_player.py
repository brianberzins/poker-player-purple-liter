import player
import json

def test_call():
    subject = player.Player()
    game_stats = json.load(open('example.json'))
    assert 240 == subject.betRequest(game_stats)