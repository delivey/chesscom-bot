from stockfish import Stockfish
from pgn_to_fen import convert_pgn

stockfish = Stockfish(path="D:\\Programs\\stockfish_15_win_x64_avx2\\stockfish_15_x64_avx2.exe", parameters={"Debug Log File": "./stockfish.log"})

def get_best_move(squares):
    global stockfish
    stockfish.make_moves_from_current_position(squares)
    best_move = stockfish.get_best_move()
    return best_move