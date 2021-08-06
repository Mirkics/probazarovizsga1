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

finally:
    driver.close()