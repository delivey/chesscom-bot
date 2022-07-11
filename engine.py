from stockfish import Stockfish

stockfish = Stockfish(path="D:\\Programs\\stockfish_15_win_x64_avx2\\stockfish_15_x64_avx2.exe", parameters={"Debug Log File": "./stockfish.log"})

def get_best_move(squares):
    global stockfish
    stockfish.make_moves_from_current_position(squares)
    best_move = stockfish.get_best_move()
    print(stockfish.get_board_visual())
    return best_move