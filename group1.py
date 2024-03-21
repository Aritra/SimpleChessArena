import chess
import random

class group1:
    def __init__(self, color):
        self.color = color
        
    def makemove(self, board):
        retmove=""
        legal_moves = board.legal_moves
        print("The list of legal moves are: ")
        print(legal_moves)
        chosen_move = random.choice(list(legal_moves))
        retmove = board.uci(chosen_move)

        return retmove