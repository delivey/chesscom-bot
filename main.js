function getMoves() {
    moves = document.getElementsByClassName('move');
    idx=1
    order = []
    PGN = ""
    for (let move of moves) {
        let madeMoves = move.children
        let moves = []
        for (let madeMove of madeMoves) {
            if (idx == 1) order.push(madeMove.classList[0])
            moves.push(madeMove.innerText)
        }
        PGN += `${idx}. ${moves[0]} ${moves[1]} `
        idx++
    }
    console.log(PGN)
}