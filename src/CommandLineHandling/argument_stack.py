from typing import Optional


class ArgumentStackIsEmpty(Exception):
    pass


class ArgumentStack:
    def __init__(self, arguments: [str]):
        self._arguments: [str] = arguments

    def _is_empty(self):
        return len(self._arguments) > 0

    def next(self) -> Optional[str]:
        if self._is_empty():
            return None
        else:
            return self._arguments[0]

    def pop(self):
        if self._is_empty():
            raise ArgumentStackIsEmpty()
        return self._arguments.pop()
