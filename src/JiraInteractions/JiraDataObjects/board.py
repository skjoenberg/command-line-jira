import string


class Board:
    def __init__(self, board):
        self._name: string = board.name
        self._id: int = board.id

    @property
    def name(self) -> string:
        return self._name

    @property
    def id(self) -> int:
        return self._id
