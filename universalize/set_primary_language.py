from .shared import Shared
from .colors import bcolors
from .errors import InvalidLanguage, SetupNotDone


class SetPrimaryLanguage:

    def __init__(self, language):
        if Shared.PyUniversalizeObject is None or Shared.DefaultLanguage is None:
            raise SetupNotDone()
        self.language = language

    def set(self):
        self._check_validations()
        Shared.DefaultLanguage = self.language
        print(f"{bcolors.OKGREEN}INFO: Primary language update to "
              f"{Shared.PyUniversalizeObject.display_name.get(self.language)}{bcolors.ENDC}")

    def _check_validations(self):
        if self.language not in Shared.PyUniversalizeObject.languages.keys():
            raise InvalidLanguage(self.language)
