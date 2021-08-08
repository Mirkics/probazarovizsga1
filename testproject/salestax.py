'''2 Feladat: Sales tax applikáció funkcióinak automatizálása
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a sales tax app-ot az https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html oldalról.
Feladatod, hogy automatizáld selenium webdriverrel a sales tax kalkulátort.

Az alábbi tesztesetekete fedd le:

TC01: üres kitöltés helyessége
nem kell ellenőrizni, hogy üresek-e a mezők, csak azt, hogy alapból a "Subtotal" feliratú gomb megnyomásakor
a salestax azonosítójú mező 0.00 értéket kell mutasson.
illetve a "Calculate Order" gomb megyomására a gtotal mező 4.95 értéket kell mutasson

TC02: 6" x 6" Volkanik Ice kitöltés helyessége
válasszuk ki a Product Item feliratú mezőből a 6" x 6" Volkanik Ice értéket
a quantity feliratú mezőbe írjunk 1-et
ellenőrizzük, hogy a "Subtotal" feliratú gomb megnyomásakor a salestax azonosítójú mező 4.95 értéket kell mutasson.
illetve a "Calculate Order" gomb megyomására a gtotal mező 9.90 értéket kell mutasson

Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest).
Egyszerűen használj elágazásokat vagy assert összehasonlításokat.'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select

options = Options()
options.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html')
    time.sleep(2)

# Mezők, gombok kikeresése

    input_qty = driver.find_element_by_id('quantity')
    input_subtotal = driver.find_element_by_id('subtotal')
    input_salestax = driver.find_element_by_id('salestax')
    total = driver.find_element_by_id('gtotal')

    btn_subtotal = driver.find_element_by_id('subtotalBtn')
    btn_calculate = driver.find_element_by_id('gtotalBtn')

# TC01: üres kitöltés helyessége
    btn_subtotal.click()
    btn_calculate.click()
    assert input_salestax.get_attribute('value') == '0.00'
    assert total.get_attribute('value') == '4.95'
    time.sleep(2)
# TC02: 6" x 6" Volkanik Ice kitöltés helyessége
    # tesztadatok
    #product_data = '6" x 6" Volkanik Ice'
    #qty = 1

    Select(driver.find_element_by_name('price')).select_by_visible_text('6" x 6" Volkanik Ice')
    input_qty.send_keys('1')
    time.sleep(2)
    btn_subtotal.click()
    time.sleep(2)
    btn_calculate.click()
    time.sleep(2)

    assert input_salestax.get_attribute('value') == '4.95'
    assert total.get_attribute('value') == '9.90'

finally:
    driver.close()