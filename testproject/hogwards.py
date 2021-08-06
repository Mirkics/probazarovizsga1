'''1 Feladat: Hogwards express jegyautomata
A Hogwards express nemrég rájött, hogy érdemes lenne önkiszolgálóvá tenni a jegykiállító rendszert a hallgatók vasútvonalán.
Lehet, hogy drágák a baglyok.

Itt találod az önkiszolgáló webes applikáció prototípusát: https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html

Készíts egy Python python applikációt (akár csak egy darab python fileban) ami selenium-ot használ.

Teszteld le, hogy az általad megadott adatokkal tölti-e ki a jegyet az applikáció.
(vigyázz, mert elkézpelhető, hogy némely adatokat egynél több helyen is megjeleníti a jegyen az applikáció)

Nem kell negatív tesztesetet készítened. Egy pozitív teszteset teljesen elég lesz.'''

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
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html')
    time.sleep(2)

finally:
    driver.close()