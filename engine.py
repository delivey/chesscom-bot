from stockfish import Stockfish
from pgn_to_fen import convert_pgn

stockfish = Stockfish(path="D:\\Programs\\stockfish_15_win_x64_avx2\\stockfish_15_x64_avx2.exe", parameters={"Debug Log File": "./stockfish.log"})
restart_times = 0

def get_best_move(PGN, restart=False):
    global stockfish
    global restart_times
    if restart:
        stockfish = Stockfish(path="D:\\Programs\\stockfish_15_win_x64_avx2\\stockfish_15_x64_avx2.exe", parameters={"Debug Log File": "./stockfish.log"})
    FEN = convert_pgn(PGN)
    fen_valid = stockfish.is_fen_valid(FEN)
    print(f"{FEN} valid: {fen_valid}")
    stockfish.set_fen_position(FEN)
    try:
        best_move = stockfish.get_best_move()
    except:
        restart_times += 1
        print(f"Stockfish crashed while returning best move. Trying to restart ({restart_times}...")
        return get_best_move(PGN, True)
    return best_move