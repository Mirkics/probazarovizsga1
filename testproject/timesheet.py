"""3 Feladat: Timesheet automatizálása
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a timesheet app-ot az https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Timesheet app tesztelését.
Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest).
Egyszerűen használj elágazásokat vagy assert összehasonlításokat.

Az alábbi tesztesetekete fedd le:
TC01: üres kitöltés helyessége
ha nincs kitoltve az e-mail mező nem lehet megnyomni a "next" feliratú gombot
ha helytelen (formailag helytelen) e-mailcimmel probáljuk kitölteni a formot nem lehet megnyomni a "next" feliratú gombot

TC02: helyes kitöltés helyes köszönet képernyő
töltsük ki a következő adatokkal a formot:
test@bela.hu
2 hours and 0 minutes
working hard
types of work: Time working on visual effects for movie
nyomjuk meg a "next" feliratú gombot
ellenőrizzük a megjelenő tartalomban az órák és percek helyességét"""

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
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html')
    time.sleep(2)

# Mezők kikeresése

    email = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[1]')\
        .get_attribute('placeholder')
    next_btn = driver.find_element_by_xpath('//*[@id="buttons"]/input').get_attribute('disabled')

    assert email == 'artist@moviemakr.com'
    assert next_btn == 'disabled'



finally:
    driver.close()