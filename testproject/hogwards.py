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

options = Options()
options.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html')
    time.sleep(2)

    # tesztadatok
    name = 'HERMIONE GRANGER'
    date = ('002021', '8', '16')
    hour = '17:25'

# tesztadatok felvitele

    driver.find_element_by_id('passenger').send_keys(name)
    driver.find_element_by_id('departure-date').send_keys(date)
    driver.find_element_by_id('departure-time').send_keys(hour)
    time.sleep(2)
    issue_ticket_button = driver.find_element_by_xpath('//*[@id="issue-ticket"]')
    issue_ticket_button.click()

#  megjelenő ticket adatok
    passenger_name = driver.find_element_by_id('passenger-name').text
    print(passenger_name)
    dep_date = driver.find_element_by_id('departure-date-text').text
    print(dep_date)
    dep_time = driver.find_element_by_id('departure-time-text').text
    print(dep_time)

    side_dep_date = driver.find_element_by_id('side-detparture-date').text
    print(side_dep_date)
    side_dep_time = driver.find_element_by_id('side-departure-time').text
    print(side_dep_time)
    time.sleep(2)
# felvitt és megjelenő adatok összehasonlítása

    assert name == passenger_name
    assert dep_date == '2021-08-16'
    assert side_dep_date == '2021-08-16'
    assert dep_time == '05:25PM'
    assert side_dep_time == '05:25PM'

finally:
    driver.close()
