"""4 Feladat: Lottoszámok automatizálása
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Lotto app-ot az https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Lotto app tesztelését.

Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest).
Egyszerűen használj elágazásokat vagy assert összehasonlításokat.

Az alábbi tesztesetekete fedd le:
TC01: lotto huzas elott nem ismertek a szamok
nem szabad, hogy akár csak egy szám is megjelenjen mielőt az első alkalommal a "Generate" feliratú gombra kattintunk

TC02: lottohuzás működik
Nyomjuk meg hatszor a "Generate" feliratú gombot
Ellenőrizzük, hogy pontosan 6db szám jelenik meg a képernyőn
Olvassuk ki a számokat és ellnőrizzük, hogy mind 1 és 59 között vannak

TC03: lottohúzás befejeződött
Nyomjuk meg 7x is a "Generate" feliratú gombot
Ellenőrizzük, hogy pontosan nem jelent meg hetedik szám
Nyomjuk meg a "Reset" feliratú gombot
nem szabad, hogy akár csak egy szám is megjelenjen miután a "Reset" gombot megnyomtuk"""

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
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html')
    time.sleep(2)

    btn_generate = driver.find_element_by_id('draw-number')
    btn_reset = driver.find_element_by_id('reset-numbers')
    section_area = driver.find_element_by_id('container').get_attribute('value')

# TC01: lotto huzas elott nem ismertek a szamok

    # assert section_area == 'empty'

# TC02: lottohuzás működik
    #6-szor meg kell nyomni a generate gombot
    for i in range(6):
        btn_generate.click()



    # assert section_area == '6' # 6 szám található azon a területen

    # egy lista kell a kihúzott számokból
    # ball_list = ()
    # számok >0 és <60

# TC03: lottohúzás befejeződött. nincs hetedik

    # assert ball_list == 6
    # btn_reset.click()
    # assert section_area == 'empty'

finally:
    driver.close()