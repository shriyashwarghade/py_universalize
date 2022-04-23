class InvalidConfig(Exception):
    def __str__(self):
        return "Config Is Not Valid"


class PrimaryLanguageNotFound(Exception):
    def __str__(self):
        return "Primary Language Config Not Found"


class InvalidConfigFormat(Exception):
    def __init__(self, file_path):
        self.file_path = file_path

    def __str__(self):
        return f"Invalid Config File Format {self.file_path}"


class FileDoesNotExists(Exception):
    def __init__(self, file_path):
        self.file_path = file_path

    def __str__(self):
        return f"File {self.file_path} does not exists"


class InvalidLanguage(Exception):
    def __init__(self, lang):
        self.lang = lang

    def __str__(self):
        return f"Invalid Language {self.lang}"


class SetupNotDone(Exception):
    def __str__(self):
        return "PyUniversalize setup is incomplete. Please use universalize.setup function to complete the setup." \
               " Refer documentation for more details"
