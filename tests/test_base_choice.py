from config_loader.loader import ConfigLoader
from config_loader.config import ConfigBaseChoice


class DummyConfig(ConfigBaseChoice):
    def __init__(self, *args, **kwargs):
        self._choices = ['foo', 'bar']
        super(DummyConfig, self).__init__(*args, **kwargs)


class DummyLoader(ConfigLoader):
    config_root_class = DummyConfig


def test_valid_choice():
    value = 'foo'
    loader = DummyLoader(value)
    assert loader.is_valid()


def test_valid_choice_whitespace():
    value = ' foo '
    loader = DummyLoader(value)
    assert loader.is_valid()


def test_valid_choice_2():
    value = 'bar'
    loader = DummyLoader(value)
    assert loader.is_valid()


def test_invalid_choice():
    value = 'deadbeef'
    loader = DummyLoader(value)
    assert not loader.is_valid()
