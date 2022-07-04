from stockfish import Stockfish
from pgn_to_fen import convert_pgn

stockfish = Stockfish(path="D:\\Programs\\stockfish_15_win_x64_avx2\\stockfish_15_x64_avx2.exe")

PGN = "1. e4 a5 2. Nc3 Ra6 3. Nf3 Re6 4. Ng5 c6 5. Bb5 Nf6 6. Nxe6 b6"
FEN = convert_pgn(PGN)

stockfish.set_fen_position(FEN)
print(stockfish.get_best_move())
# print(stockfish.get_board_visual())