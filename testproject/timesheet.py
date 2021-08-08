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

    email = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[1]')
    next_btn = driver.find_element_by_xpath('//*[@id="buttons"]/input')

    assert email.get_attribute('placeholder') == 'artist@moviemakr.com'
    assert next_btn.get_attribute('ng-disabled') == 'formTimesheet.$invalid'

# helytelen email cím 'valaki@@valaki.com'

    email.send_keys('valaki@@valaki.com')
    time.sleep(1)
    next_btn.click()

    assert next_btn.get_attribute('ng-disabled') == 'formTimesheet.$invalid'

    email.clear()

# TC02: helyes kitöltés helyes köszönet képernyő
    #test@bela.hu
    #2 hours and 0 minutes
    #working hard
    #types of work: Time working on visual effects for movie

    email.send_keys('test@bela.hu')

    time_hour = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[2]')
    time_hour.send_keys('2')
    time_min = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[3]')
    time_min.send_keys('0')
    message = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/textarea')
    message.send_keys('working hard')
    types_of_work = driver.find_element_by_xpath('//*[@id="dropDown"]')
    types_of_work.send_keys('Time working on visual effects for movie')
    time.sleep(1)
    next_btn.click()
    time.sleep(2)
    thanks = driver.find_elements_by_xpath('//*[@id="section-thankyou"]/div/p[1]')

    #assert thanks == 'Thank you' + email

    hour_check = driver.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[2]/span[1]').get_attribute('value')
    min_check = driver.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[2]/span[2]').get_attribute('value')
    assert time_hour == hour_check
    assert time_min == min_check

finally:
    driver.close()