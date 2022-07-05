from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.chess.com/play/computer")

finish = input("Finished setup?")

JS_getPGN = """
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

ans = driver.execute_script(JS_getPGN)
print(ans)

# driver.close()