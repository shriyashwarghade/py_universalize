from .errors import SetupNotDone
from .shared import Shared


class GetLanguages:

    def __init__(self):
        if Shared.PyUniversalizeObject is None or Shared.DefaultLanguage is None:
            raise SetupNotDone()

    def get(self):
        py_uni_obj = Shared.PyUniversalizeObject
        data = []
        for lang in py_uni_obj.languages:
            data.append({
                'display_name': py_uni_obj.display_name.get(lang),
                'code': lang,
                'is_primary': True if lang == Shared.DefaultLanguage else False
            })
        return data
