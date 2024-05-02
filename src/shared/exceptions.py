



class SettingsError(Exception):
    """ a base class for settings exceptions """

class SettingsFileNotExist(SettingsError):
    """ a custom exception raised when loading settings file """

class SettingsFileInvalid(SettingsError):
    """ a custom exception raised when decoding settings file """

class SettingsDataInvalid(SettingsError):
    """ a custom exception raised when validating settings data """


class ConnectError(Exception):
    """ a base class for connect exceptions """

class ConnectIpUsernamePasswordEmpty(ConnectError):
    """ """

class ConnectUsernamePasswordWrong(ConnectError):
    """ """

class ConnectPasswordOverrun(ConnectError):
    """ """

class ConnectRequestTimeout(ConnectError):
    """ """