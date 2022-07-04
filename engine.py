from stockfish import Stockfish

stockfish = Stockfish(path="D:\\Programs\\stockfish_15_win_x64_avx2\\stockfish_15_x64_avx2.exe")

PGN = "1. e4 a5 2. Nc3 Ra6 3. Nf3 Re6 4. Ng5 c6 5. Bb5 Nf6"
split = PGN.split(" ")
for i in split:
    if i[0].isdigit() and i[1] == ".":
        split.remove(i)

moves = [ ''.join(x) for x in zip(split[0::2], split[1::2]) ]
print(split)



stockfish.set_fen_position("1nbqkb1r/1p1ppppp/2p1rn2/pB4N1/4P3/2N5/PPPP1PPP/R1BQK2R w - KQkq")
print(stockfish.get_best_move())
print(stockfish.get_board_visual())