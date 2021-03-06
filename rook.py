from piece import Piece
import numpy as np


class Rook(Piece):
    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self.position = np.array([-1, -1])
        self.type = "Rook"

    def get_moves(self, board):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        moves = self.find_moves_from_movement_vectors(board=board,
                                                      directions=directions,
                                                      can_step_multiple=True,
                                                      incremental_sum=1)
        return moves

    def move_to_position(self, position):
        self.position = position
