
from abc import ABCMeta, abstractmethod
import numpy as np

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

    def find_moves_from_movement_vectors(self, board, directions, can_step_multiple, incremental_sum=1):
        moves = []
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

                if can_step_multiple:
                    incremental_step = incremental_sum * direction / np.abs(direction).sum()
                    directions.append(direction + incremental_step)
        return moves

    def __str__(self):
        return f"Type: {self.type}, Owner: {self.owner}, ID: {self.id}, Position: {self.position}"
