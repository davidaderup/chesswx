import numpy as np
from copy import deepcopy


class Board:

    def __init__(self):
        self.current_board_state = []
        self.board_states = []
        self.board_size = np.array((8, 8))

    def create_empty_state(self):
        empty_state = {}
        self.current_board_state = empty_state

    def place_piece_on_board(self, piece, position):
        if self.is_out_of_bounds(position):
            raise ValueError(f"Position {position} is out of bounds.")

        if self.is_occupied(position):
            raise ValueError(f"Position {position} is occupied by another piece.")
        self.board_states.append(deepcopy(self.current_board_state))
        self.current_board_state.append(piece)
        piece.move_to_position(position)

    def is_occupied(self, position):
        for piece in self.current_board_state:
            if np.array_equal(piece.position, position):
                return True
        return False

    def is_out_of_bounds(self, position):
        upper_check = position >= self.board_size
        lower_check = position < np.zeros(2)
        checks = np.append(upper_check, lower_check)
        return np.any(checks)

    def __str__(self):
        board_mat = np.zeros(self.board_size)
        for piece in self.current_board_state:
            board_mat[piece.position[0], piece.position[1]] = piece.id
        return str(board_mat)

    def get_piece_by_id(self, piece_id):
        for piece in self.current_board_state:
            if piece_id == piece.id:
                return piece
        raise ValueError("ID does not match any piece on board.")

    def get_piece_by_position(self, position):
        for piece in self.current_board_state:
            if np.array_equal(piece.position, position):
                return piece
        raise ValueError("No piece can be found at the position.")

    def get_binary_map_of_moves_for_piece(self, piece):
        moves = piece.get_moves(self)
        board_mat = self.get_binary_map_from_positions(moves)
        return board_mat

    def get_guarded_positions(self, owner):
        guarded_positions = []
        for piece in self.current_board_state:
            if piece.owner == owner:
                moves = piece.get_moves(self)
                guarded_positions.extend(moves)
        guarded_positions = np.unique(guarded_positions, axis=0)
        return guarded_positions

    def get_binary_map_from_positions(self, moves):
        board_mat = np.zeros(self.board_size)
        for move in moves:
            board_mat[move[0], move[1]] = 1
        return board_mat

    @staticmethod
    def get_positions_from_binary_map(binary_map):
        positions_x, positions_y = np.nonzero(binary_map)
        positions = [np.array([position_x, position_y]) for position_x, position_y in zip(positions_x, positions_y)]
        return positions

    @staticmethod
    def get_opponent(owner):
        if owner == "Black":
            return "White"
        else:
            return "Black"

