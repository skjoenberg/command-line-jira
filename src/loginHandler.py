import keyring
from constants import Constants 
from commandLineHandler import WriteToConsole, ReadFromConsole

class LoginHandler():
    def __init__(self, username: str):
        self._username = username 
        self._password = self._resolvePassword()

    def _resolvePassword(self):
        passwordFromKeyring = self._tryFetchPassword()
        if passwordFromKeyring:
            return passwordFromKeyring 
        else:
            passwordFromConsole = self._requirePasswordFromInput()
            self._storePassword(passwordFromConsole)
            return passwordFromConsole
        
    def _tryFetchPassword(self):
        return keyring.get_password(Constants.KEYRING_ID, self._username)

    def _requirePasswordFromInput(self):
       WriteToConsole("Enter password")
       password = ReadFromConsole()
       return password 

    def _storePassword(self, password: str):
        keyring.set_password(Constants.KEYRING_ID, self._username, password)

    def getAuthentication(self):
        return (self._username, self._password)