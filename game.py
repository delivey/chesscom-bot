from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from engine import get_best_move

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

pgn = driver.execute_script(JS_getPGN)
move = get_best_move(pgn)
print(move)

idx = 1
while True:
    idx += 1
    try:
        next = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'div[data-ply="{idx*2}"]')))
        pgn = str(driver.execute_script(JS_getPGN)).rstrip().lstrip()
        print(pgn)
        move = get_best_move(pgn)
        print(move)
    except KeyboardInterrupt:
        break

# driver.close()