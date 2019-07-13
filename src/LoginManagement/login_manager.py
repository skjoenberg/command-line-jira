import keyring

from Config.config_manager import ConfigManager
from constants import Constants
from CommandLine.command_line_utilities import require_password_from_input


class LoginManager:
    def __init__(self, config_manager: ConfigManager):
        """Initializes the login manager"""
        self._username = config_manager.username
        self._password = None
        self._resolve_password()

    def _resolve_password(self):
        """Checks whether a password exists in the credentials (RAM).
        Otherwise, asks for a password through the command line."""
        try:
            self._password = self._fetch_password_from_credentials()
        except CredentialsPasswordNotFound:
            self.read_and_store_password_from_console()
            pass

    def _fetch_password_from_credentials(self):
        """Fetches password from credentials (RAM)"""
        password = keyring.get_password(Constants.KEYRING_ID, self._username)

        if password is None:
            raise CredentialsPasswordNotFound

        return password

    def read_and_store_password_from_console(self) -> None:
        """Asks for a password through the command line"""
        password_from_console = require_password_from_input()
        self._store_password_in_credentials(password_from_console)
        self._password = password_from_console

    def _store_password_in_credentials(self, password: str):
        """Stores the password in credentials (RAM)"""
        keyring.set_password(Constants.KEYRING_ID, self._username, password)

    def get_login_information(self):
        """Gets the username and password"""
        return self._username, self._password


class CredentialsPasswordNotFound(Exception):
    """Password not found in credentials"""
    pass


