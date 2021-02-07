
from abc import ABCMeta, abstractmethod


class Piece():
    def __init__(self, id, owner):
        self.position = (-1, -1)
        self.id = id
        self.type = "Piece"
        self.owner = owner

    @abstractmethod
    def get_moves(self, board):
        pass

    @abstractmethod
    def move_to_position(self, position):
        self.position = position

    def __str__(self):
        return f"Type: {self.type}, Owner: {self.owner}, ID: {self.id}, Position: {self.position}"
