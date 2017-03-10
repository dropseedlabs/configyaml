from .base import ConfigBase


class ConfigBaseChoice(ConfigBase):
    def __init__(self, *args, **kwargs):
        self._type = str
        # class should specify self._choices = []  # list of choices that the str can be
        super(ConfigBaseChoice, self).__init__(*args, **kwargs)

    def _validate(self):
        super(ConfigBaseChoice, self)._validate()

        if not self.is_valid():
            return

        if self._value not in self._choices:
            self._add_error(
                title='Invalid choice',
                description='Must be one of {}'.format(self._choices),
            )