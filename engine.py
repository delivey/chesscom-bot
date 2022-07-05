from stockfish import Stockfish
from pgn_to_fen import convert_pgn

stockfish = Stockfish(path="D:\\Programs\\stockfish_15_win_x64_avx2\\stockfish_15_x64_avx2.exe")

def get_best_move(PGN):
    FEN = convert_pgn(PGN)
    print("Converted PGN")
    print(FEN)

    stockfish.set_fen_position(FEN)
    print(stockfish.get_board_visual())
    return stockfish.get_best_move()
