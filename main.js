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