from piece import Piece
import numpy as np


class Rook(Piece):
    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self.position = np.array([-1, -1])
        self.type = "Rook"

    def get_moves(self, board):
        moves = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        direction_ind = -1

        while direction_ind + 1 < len(directions):
            direction_ind += 1
            direction = np.array(directions[direction_ind])

            new_position = self.position + direction
            new_position = new_position.astype(int)
            if board.is_out_of_bounds(new_position):
                continue
            if board.is_occupied(new_position):
                occupying_piece = board.get_piece_by_position(new_position)
                if occupying_piece.owner != self.owner:
                    moves.append(new_position)
                continue
            else:
                moves.append(new_position)
                incremental_step = direction / np.abs(direction.sum())
                directions.append(direction + incremental_step)
        return moves

    def move_to_position(self, position):
        self.position = position
