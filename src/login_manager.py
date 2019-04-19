import keyring
from constants import Constants
from command_line_utilities import require_password_from_input


class LoginManager:
    def __init__(self, username: str):
        self._username = username
        self._password = None

        self._resolve_password()

    def _resolve_password(self):
        try:
            self._password = self._fetch_password_from_credentials()
        except CredentialsPasswordNotFound:
            self.read_and_store_password_from_console()
            pass

    def _fetch_password_from_credentials(self):
        password = keyring.get_password(Constants.KEYRING_ID, self._username)

        if password is None:
            raise CredentialsPasswordNotFound

        return password

    def read_and_store_password_from_console(self) -> None:
        password_from_console = require_password_from_input()
        self._store_password_in_credentials(password_from_console)
        self._password = password_from_console

    def _store_password_in_credentials(self, password: str):
        keyring.set_password(Constants.KEYRING_ID, self._username, password)

    def get_login_information(self):
        return self._username, self._password


class CredentialsPasswordNotFound(Exception):
    """Password not found in credentials"""
    pass


