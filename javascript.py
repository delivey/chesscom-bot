import string

JS_getLastMoveNums = """
highlighted = document.querySelectorAll('div[data-test-element="highlight"]')
squares = []
reverseList = false
idx = 0

for (square of highlighted) {
    square = square.classList[1].replace("square-", "") // 77, 64, etc.
    allPiecesOnSquare = document.getElementsByClassName(`square-${square}`)
    piecesOnSquare = []
    
    for (piece of allPiecesOnSquare) {
        if (!piece.classList.contains("bot-made")) piecesOnSquare.push(piece)
    }

    if (piecesOnSquare.length > 0) { squares.push(square) }
    else { continue }

    // Actual code for pieces 
    console.log(square, piecesOnSquare.length, squares, idx)
    squareHasPiece = piecesOnSquare.length > 1
    if (!squareHasPiece && square !== squares[0]) reverseList = true

    idx++
}
if (reverseList) {
    squares.reverse()
}

new_squares = []
const alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
for (square of squares) { // square - 55, 77, etc.
    new_squares.push(alphabet[parseInt(square[0])-1] + square[1])
}
let full = new_squares.join("")

moves = document.getElementsByClassName("move")
last_move = moves[moves.length-1]
let children = last_move.children
let move = children[children.length-1].innerText
if (move.includes("=")) {
    console.log("promoting")
    full += move.split("=")[1].toLowerCase();
} else { promotion = false }

return full
"""

def convertSquare(square):
    first = str(string.ascii_lowercase.index(square[0]) + 1)
    second = str(square[1])
    return first + second

def JS_highlightSquare(square, color):
    num = convertSquare(square)
    js = f"""
    const newSquare = document.createElement("div");
    newSquare.setAttribute("id", {num});
    newSquare.classList.add(`square-{num}`);
    newSquare.classList.add("highlight");
    newSquare.classList.add("bot-made")
    newSquare.style.backgroundColor = "{color}";
    newSquare.style.opacity = 0.5
    newSquare.dataset.testElement = "highlight"
    document.querySelector("chess-board").appendChild(newSquare); 
    """
    return js

def JS_removeHighlight(square):
    num = convertSquare(square)
    js = f"""
    let sqr = document.getElementById({num})
    sqr.parentNode.removeChild(sqr);
    """
    return js
