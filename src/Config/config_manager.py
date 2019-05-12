from constants import Constants
from Config.config import Config
from typing import Optional
from CommandLine.command_line_utilities import require_input, write_to_console
import json

home = str()


class ConfigManager:
    _config: Optional[Config]

    def __init__(self):
        self._config = None

        try:
            self._read_config()
        except FileNotFoundError:
            self._set_config(*self._require_config_parameters_from_console())
            self._write_config()

    def _read_config(self) -> None:
        with open(Constants.CONFIG_PATH) as config_file:
            config_parameters = self._translate_json_to_config(config_file.read())
            self._set_config(*config_parameters)

    @staticmethod
    def _require_config_parameters_from_console() -> (str, str):
        write_to_console("Config not found - Creating config")
        config_parameters = ()
        for input_message in ["Enter " + parameter + ":" for parameter in ["username", "default board", "server"]]:
            write_to_console(input_message)
            config_parameters += (require_input("Enter username:"),)
        return config_parameters

    def _set_config(self, *config_parameters):
        self._config = Config(*config_parameters)

    def _write_config(self):
        try:
            with open(Constants.CONFIG_PATH, "w+") as config_file:
                print(self._translate_config_to_json())
                config_file.write(self._translate_config_to_json())
        except Exception as e:
            print(e)
            pass

    def _translate_config_to_json(self) -> str:
        return json.dumps([{
            'username': self._config.username,
            'default_board': self._config.default_board,
            'server': self._config.server
        }], separators=(',', ':'))

    @staticmethod
    def _translate_json_to_config(json_string):
        try:
            json_dict = json.loads(json_string)[0]
            return json_dict["username"], json_dict["default_board"], json_dict["server"]
        except:
            pass

    def get_username(self):
        return self._config.username

    def get_default_board(self):
        return self._config.default_board
