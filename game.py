from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from engine import get_best_move
from javascript import JS_getPgn, JS_highlightSquare

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://www.chess.com/play/computer")

finish = input("Finished setup?\n")

pgn = driver.execute_script(JS_getPgn)
move = get_best_move(pgn)
print(move)

idx = 1
while True:
    idx += 1
    try:
        next = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'div[data-ply="{idx*2}"]')))
        pgn = str(driver.execute_script(JS_getPgn)).rstrip().lstrip()
        move = get_best_move(pgn)
        squares = [move[i:i+2] for i in range(0, len(move), 2)]
        print(move)
        print(squares)
        driver.execute_script(JS_highlightSquare(squares[0], "blue"))
        driver.execute_script(JS_highlightSquare(squares[1], "red"))
    except KeyboardInterrupt:
        break

# driver.close()
