import pgntofen

def convert_pgn(pgn):
    split = pgn.split(" ")
    for i in split:
        if i[0].isdigit() and i[1] == ".":
            split.remove(i)

    pgnConverter = pgntofen.PgnToFen()
    PGNMoves = split
    pgnConverter.pgnToFen(PGNMoves)
    fen = pgnConverter.getFullFen()
    return fen