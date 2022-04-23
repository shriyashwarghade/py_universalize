import json

from .colors import bcolors
from .shared import Shared
from .errors import InvalidLanguage, SetupNotDone


class Locale:
    def __init__(self, text, language):
        if Shared.PyUniversalizeObject is None or Shared.DefaultLanguage is None:
            raise SetupNotDone()
        self.text = text
        self.language = language

    def locale_string(self):
        self._check_validations()
        return self._convert()

    def _check_validations(self):
        if not self.language:
            self.language = Shared.DefaultLanguage
        if self.language not in Shared.PyUniversalizeObject.languages.keys():
            raise InvalidLanguage(self.language)

    def _convert(self):
        with open(Shared.PyUniversalizeObject.languages.get(self.language), 'rb') as f:
            data = json.loads(f.read())
        text = data
        for i in self.text.split('.'):
            text = text.get(i, {})
        if not text or text == {}:
            if not self.language == Shared.DefaultLanguage:
                print(
                    f"{bcolors.WARNING}WARNING: Translation for {self.text} not found"
                    f" in language {Shared.PyUniversalizeObject.display_name.get(self.language)} "
                    f"trying for primary language{bcolors.ENDC}")
                self.language = Shared.DefaultLanguage
                return self.locale_string()
            print(f"{bcolors.WARNING}WARNING: Translation for {self.text} not found "
                  f"in primary language {Shared.PyUniversalizeObject.display_name.get(self.language)}{bcolors.ENDC}")
            return self.text
        return text
