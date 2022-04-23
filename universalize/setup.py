import json
from pathlib import Path

from .colors import bcolors

from .py_universalize import PyUniversalize
from .errors import InvalidConfigFormat, FileDoesNotExists, PrimaryLanguageNotFound
from .shared import Shared


# TODO change ERROR FOR FILE FORMAT

class Setup:
    def __init__(self, config):
        self.config = config
        self._setup()

    def _setup(self):
        if not isinstance(self.config, dict):
            if not Path(self.config).suffix == '.json':
                raise InvalidConfigFormat(self.config)
            if not Path(self.config).exists():
                raise FileDoesNotExists(self.config)
            with open(self.config, 'rb') as f:
                self.config = json.loads(f.read())

        if not self.config.get('primary'):
            raise PrimaryLanguageNotFound()
        self._check_file_exists()
        primary = self.config.get('primary').get('code')
        display_name = {self.config.get('primary').get('code'): self.config.get('primary').get('display_name')}
        languages = {self.config.get('primary').get('code'): self.config.get('primary').get('file')}
        for lang in self.config.get('languages', []):
            languages.update({lang.get('code'): lang.get('file')})
            display_name.update({lang.get('code'): lang.get('display_name')})

        Shared.PyUniversalizeObject = PyUniversalize(self.config, primary, languages, display_name)
        Shared.DefaultLanguage = primary
        print(f"{bcolors.OKGREEN}INFO: PyUniversalize Setup Completed{bcolors.ENDC}")

    def _check_file_exists(self):
        if not Path(self.config.get('primary').get('file')).exists():
            if not Path(self.config.get('primary').get('file')).suffix == '.json':
                raise InvalidConfigFormat(self.config.get('primary').get('file'))
            raise FileDoesNotExists(self.config.get('primary').get('file'))

        for lang in self.config.get('languages', []):
            if not Path(lang.get('file')).suffix == '.json':
                raise InvalidConfigFormat(lang.get('file'))
            if not Path(lang.get('file')).exists():
                raise FileDoesNotExists(lang.get('file'))
