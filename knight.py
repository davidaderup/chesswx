from piece import Piece
import numpy as np


class Knight(Piece):
    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self.position = np.array([-1, -1])
        self.type = "Knight"

    def get_moves(self, board):
        directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        moves = self.find_moves_from_movement_vectors(board=board,
                                                      directions=directions,
                                                      can_step_multiple=False,
                                                      incremental_sum=3)
        return moves

    def move_to_position(self, position):
        self.position = position
