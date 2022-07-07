import os
from DotenvLibrary import DotenvLibrary


def test_set_env():
    assert os.getenv("KEY_1") == None
    key_list = ["KEY_1", "KEY_2"]
    DotenvLibrary.set_env_var(DotenvLibrary, key_list)
    assert os.getenv("KEY_1") != None
    assert os.getenv("KEY_1") == "Hello"
    assert os.getenv("KEY_2") != None
    assert os.getenv("KEY_2") == "World"