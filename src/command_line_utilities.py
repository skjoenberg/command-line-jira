from getpass import getpass
from typing import Callable


def write_to_console(message: str) -> None:
    print(message)


def read_from_console() -> str:
    return input()


def require_input(error_message: str, input_function: Callable[[], str] = read_from_console) -> str:
    while True:
        console_input: str = input_function()
        if not console_input:
            write_to_console(error_message)
        else:
            return console_input


def require_password_from_input() -> str:
    write_to_console("Enter password:")
    password: str = require_input("No password entered, please enter password:", getpass)
    return password
