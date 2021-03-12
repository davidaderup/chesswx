from piece import Piece
import numpy as np


class Pawn(Piece):
    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self.position = np.array([-1, -1])
        self.type = "Pawn"

    def get_moves(self, board):
        directions = []

        if self.owner == "White":
            moving_direction = 1
            start_position = 1
        else:
            moving_direction = -1
            start_position = 6

        # Normal movement
        normal_direction = np.array([moving_direction * 1, 0])
        if not board.is_occupied(self.position + normal_direction):
            directions.append(normal_direction)
        # Starting position condition
        if self.position[0] == start_position:
            starting_direction = np.array([moving_direction * 2, 0])
            if not board.is_occupied(self.position + starting_direction):
                directions.append(starting_direction)
        # Capture moves
        capture_directions = [np.array([moving_direction * 1, 1]), np.array([moving_direction * 1, -1])]
        for capture_direction in capture_directions:
            capture_position = self.position + capture_direction
            if board.is_occupied(capture_position):
                occupying_piece = board.get_piece_by_position(position=capture_position)
                if occupying_piece.owner == board.get_opponent(self.owner):
                    directions.append(capture_direction)

        moves = np.add(self.position, directions)
        return moves

    def move_to_position(self, position):
        self.position = position
