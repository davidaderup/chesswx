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
            # Normal movement
            normal_direction = np.array([1, 0])
            if not board.is_occupied(self.position + normal_direction):
                directions.append(normal_direction)
            # Starting position condition
            if self.position[0] == 1:
                starting_direction = np.array([2, 0])
                if not board.is_occupied(self.position + starting_direction):
                    directions.append(starting_direction)
            # Capture moves
            capture_directions = [np.array([1, 1]), np.array([1, -1])]
            for capture_direction in capture_directions:
                capture_position = self.position + capture_direction
                if board.is_occupied(capture_position):
                    occupying_piece = board.get_piece_by_position(position=capture_position)
                    if occupying_piece.owner == board.get_opponent(self.owner):
                        directions.append(capture_direction)
        else:
            # Normal movement
            normal_direction = np.array([-1, 0])
            if not board.is_occupied(self.position + normal_direction):
                directions.append(normal_direction)
            # Starting position movement
            starting_direction = np.array([-2, 0])
            if not board.is_occupied(self.position + starting_direction):
                directions.append(starting_direction)
            # Capture moves
            capture_directions = [np.array([-1, 1]), np.array([-1, -1])]
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
