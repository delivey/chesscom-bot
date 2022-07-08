import string

JS_getPgn = """
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
return PGN
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
