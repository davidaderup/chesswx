from piece import Piece
import numpy as np


class King(Piece):
    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self.position = np.array([-1, -1])
        self.type = "Queen"

    def get_moves(self, board):
        # Straight Moves
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        moves = self.find_moves_from_movement_vectors(board=board,
                                                      directions=directions,
                                                      can_step_multiple=False,
                                                      incremental_sum=1)
        # Diagonal Moves
        directions = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
        diag_moves = self.find_moves_from_movement_vectors(board=board,
                                                           directions=directions,
                                                           can_step_multiple=False,
                                                           incremental_sum=2)
        moves.extend(diag_moves)

        return moves

    def move_to_position(self, position):
        self.position = position
