from .get_languages import GetLanguages
from .locale import Locale
from .set_primary_language import SetPrimaryLanguage
from .setup import Setup
from .shared import Shared


def setup(config) -> None:
    """
    :param config: Dict or Config File Location in str format
    example: {
              "primary": {
                "code": "en",
                "file": "en.json",
                "display_name": "English"
              },
              "languages": [
                {
                  "code": "fr",
                  "file": "fr.json",
                  "display_name": "French"
                }
              ]
            }
    :return: None
    """
    Setup(config)


def locale(text, language_code=None) -> str:
    """
    Gets the translated value of a key.Fallback to primary language when translations are missing on the current lang
    :param text: Dot notated string
    :param language_code: (Optional) Language code to translate. If None primary language is selected.
    :return: The translated key
    """
    return Locale(text, language_code).locale_string()


def get_languages() -> list:
    """
    Returns an array of currently available languages
    example: [{'display_name': 'English', 'code': 'en', 'is_primary': True},
            {'display_name': 'French', 'code': 'fr', 'is_primary': False}]
    """
    return GetLanguages().get()


def set_primary_language(code) -> None:
    """
    Sets the primary language
    :param code: Language Code
    :return: None
    """
    SetPrimaryLanguage(code).set()
