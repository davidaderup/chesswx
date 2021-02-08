from piece import Piece
import numpy as np


class Pawn(Piece):
    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self.position = np.array([-1, -1])
        self.type = "Pawn"

    def get_moves(self, board):
        if self.owner == "White":
            normal_direction = np.array([1, 0])
        else:
            normal_direction = np.array([-1, 0])

        normal_move = self.position + normal_direction
        moves = [normal_move]

        return moves

    def move_to_position(self, position):
        self.position = position
