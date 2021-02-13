from piece import Piece
import numpy as np


class King(Piece):
    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self.position = np.array([-1, -1])
        self.type = "King"

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



        opponent = board.get_opponent(self.owner)
        guarded_positions = board.get_guarded_positions(opponent)

        guarded_mat = board.get_binary_map_from_positions(moves=guarded_positions)
        moves_mat = board.get_binary_map_from_positions(moves=moves)
        free_mat = np.logical_not(guarded_mat)
        available_moves_mat = np.logical_and(moves_mat, free_mat)
        moves = board.get_positions_from_binary_map(available_moves_mat)

        return moves

    def move_to_position(self, position):
        self.position = position
