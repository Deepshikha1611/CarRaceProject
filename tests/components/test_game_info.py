import time
import pytest
from src.components import GameInfo  
 
@pytest.fixture
def game_info():
    return GameInfo()
 
def test_next_level(game_info):
    game_info.next_level()
    assert game_info.level == 2
    assert not game_info.started
    assert game_info.level_start_time == 0
 
def test_reset(game_info):
    game_info.reset()
    assert game_info.level == 1
    assert not game_info.started
    assert game_info.level_start_time == 0
 
def test_game_finished(game_info):
    assert not game_info.game_finished()
    game_info.level = 4
    assert game_info.game_finished()
 
def test_start_level(game_info):
    game_info.start_level()
    assert game_info.started
    assert game_info.level_start_time != 0
 
def test_get_level_time(game_info, monkeypatch):
    monkeypatch.setattr(time, 'time', lambda: 10.5)
    game_info.start_level()
    assert game_info.get_level_time() == 11  
