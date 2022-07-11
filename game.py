from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from engine import get_best_move
from javascript import JS_highlightSquare, JS_removeHighlight, JS_getLastMoveNums

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://www.chess.com/play/computer")

finish = input("Finished setup?\n")

# Recommendation for best move
driver.execute_script(JS_highlightSquare("e2", "blue"))
driver.execute_script(JS_highlightSquare("e4", "red"))

idx = 0
while True:
    idx += 1
    try:
        if idx == 2:
            driver.execute_script(JS_removeHighlight("e2"))
            driver.execute_script(JS_removeHighlight("e4"))
        all_squares = []
        own_next = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'div[data-ply="{(idx*2)-1}"]')))
        last_move_nums = driver.execute_script(JS_getLastMoveNums)
        print(last_move_nums)
        all_squares.append(last_move_nums)
        next = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'div[data-ply="{idx*2}"]')))
        try:
            driver.execute_script(JS_removeHighlight(squares[0]))
            driver.execute_script(JS_removeHighlight(squares[1]))
        except Exception as e:
            print(e)

        last_move_nums = driver.execute_script(JS_getLastMoveNums)
        print(last_move_nums)
        all_squares.append(last_move_nums)

        print(all_squares)

        # pgn = str(driver.execute_script(JS_getPgn)).rstrip().lstrip()
        move = get_best_move(all_squares)
        print(move)
        squares = [move[i:i+2] for i in range(0, len(move), 2)]
        driver.execute_script(JS_highlightSquare(squares[0], "blue"))
        driver.execute_script(JS_highlightSquare(squares[1], "red"))
    except KeyboardInterrupt:
        break

# driver.close()
