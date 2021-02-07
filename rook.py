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

        # Get horizontal moves
        position_ind = self.position[0]
        while position_ind + 1 < board.board_size[0]:
            position_ind += 1
            if position_ind == self.position[0]:
                continue
            new_position = np.array([position_ind, self.position[1]])
            if board.is_occupied(new_position):
                blocking_piece = board.get_piece_by_position(new_position)
                if blocking_piece.owner == self.owner:
                    break
                else:
                    moves.append(new_position)
                    break
            moves.append(new_position)

        position_ind = self.position[0]
        while position_ind - 1 >= 0:
            position_ind -= 1
            if position_ind == self.position[0]:
                continue
            new_position = np.array([position_ind, self.position[1]])
            if board.is_occupied(new_position):
                blocking_piece = board.get_piece_by_position(new_position)
                if blocking_piece.owner == self.owner:
                    break
                else:
                    moves.append(new_position)
                    break
            moves.append(new_position)


        # Get vertical moves
        position_ind = self.position[1]
        while position_ind + 1 < board.board_size[1]:
            position_ind += 1
            if position_ind == self.position[1]:
                continue
            new_position = np.array([self.position[0], position_ind])

            if board.is_occupied(new_position):
                blocking_piece = board.get_piece_by_position(new_position)
                if blocking_piece.owner == self.owner:
                    break
                else:
                    moves.append(new_position)
                    break
            moves.append(new_position)

        position_ind = self.position[1]
        while position_ind - 1 >= 0:
            position_ind -= 1
            if position_ind == self.position[1]:
                continue
            new_position = np.array([self.position[0], position_ind])
            if board.is_occupied(new_position):
                blocking_piece = board.get_piece_by_position(new_position)
                if blocking_piece.owner == self.owner:
                    break
                else:
                    moves.append(new_position)
                    break
            moves.append(new_position)

        return moves

    def move_to_position(self, position):
        self.position = position
