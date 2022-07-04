import pgntofen

pgnConverter = pgntofen.PgnToFen()
PGNMoves = ['e4', 'a5', 'Nc3', 'Ra6', 'Nf3', 'Re6', 'Ng5', 'c6', 'Bb5', 'Nf6']
pgnConverter.pgnToFen(PGNMoves)
fen = pgnConverter.getFullFen()
print(fen)
#fen will be 'rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR - KQkq'