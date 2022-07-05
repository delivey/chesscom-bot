import pgntofen

def convert_pgn(pgn):
    clean_pgn = pgn.rstrip()
    split = clean_pgn.split(" ")
    for i in split:
        if i[0].isdigit() and i[1] == ".": split.remove(i)

    pgnConverter = pgntofen.PgnToFen()

    pgnConverter.resetBoard()
    pgnConverter.fens = []
    
    pgnConverter.pgnToFen(split)
    fen = pgnConverter.getFullFen()
    return fen

# print(convert_pgn("1. e4 b6 2. Nc3 c6"))