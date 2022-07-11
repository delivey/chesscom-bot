function getMoves() {
    moves = document.getElementsByClassName('move');
    idx=1
    PGN = ""
    for (let move of moves) {
        let madeMoves = move.children
        let moves = []
        for (let madeMove of madeMoves) {
            let moving = ""
            try {
                moving += madeMove.children[0].dataset.figurine
            } catch (e) {}
            moving += madeMove.innerText
            moves.push(moving)
        }
        PGN += `${idx}. ${moves[0]} ${moves[1]} `
        idx++
    }
    console.log(PGN)
}

function highlightSquare(num, color) {
    const newSquare = document.createElement("div");
    newSquare.setAttribute("id", num);
    newSquare.classList.add(`square-${num}`);
    newSquare.classList.add("highlight");
    newSquare.style.backgroundColor = color;
    newSquare.style.opacity = 0.5
    newSquare.dataset.testElement = "highlight"
    document.querySelector("chess-board").appendChild(newSquare); 
}

function removeHighlight(num) {
    let sqr = document.getElementById(num)
    sqr.parentNode.removeChild(sqr);
}

function getSquares() {
    squares = []
    sq = document.querySelectorAll('div[data-test-element="highlight"]')
    for (s of sq) {
        squares.push(s.classList[1].replace("square-", ""))
    }
    return squares
}


sq = document.querySelectorAll('div[data-test-element="highlight"]')
squares = []
reverseList = false
idx = 0
for (s of sq) {
    square = s.classList[1].replace("square-", "")
    // For first iteration
    if (idx == 0 || idx == 1) {
        piecesOnSquare = document.getElementsByClassName(`square-${square}`)
        console.log(square, piecesOnSquare.length)
        squareHasPiece = piecesOnSquare.length > 1
        if (squareHasPiece) reverseList = true
    }
    squares.push(square)
    idx++
}
if (reverseList) {
    console.log("reversing")
    squares.reverse()
}
// return squares


highlighted = document.querySelectorAll('div[data-test-element="highlight"]')
squares = []
reverseList = false
idx = 0

for (square of highlighted) {
    square = square.classList[1].replace("square-", "") // 77, 64, etc.
    squares.push(square)

    piecesOnSquare = document.getElementsByClassName(`square-${square}`)
    squareHasPiece = piecesOnSquare.length > 1
    if (!squareHasPiece && square !== squares[0]) reverseList = true

    idx++
}
if (reverseList) {
    console.log("reversing")
    squares.reverse()
}
console.log(squares)
// return squares

