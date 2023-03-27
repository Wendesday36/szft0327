from selenium import webdriver
from selenium.webdriver.common.by import By

def validalas():
    # Hozz létre egy Firefox driver példányt!
    driver = webdriver.Firefox()

    # Töltse be az oldaladat
    driver.get("http://localhost/szft0327/")

    # A nevek alapján kerestessük meg az űrlap elemeit!
    f_nev = driver.find_element(By.NAME,"fnev")
    jelszo = driver.find_element(By.NAME,"jsz")
    email = driver.find_element(By.NAME,"mail")
    # ... 
    # A következő elemet nem kell átírnod:
    submit_gomb = driver.find_element(By.XPATH,"//input[@type='submit']")

    # Add meg a működő - majd később a nem működő - teszt adatokat!
    f_nev.send_keys("John")
    jelszo.send_keys("Lma123")
    email.send_keys("vami@vmi.hu")
    # ...

    # Kattints a submit gombra!
    submit_gomb.click()

    # Várunk egy keveset, hogy lássunk is valamit...
    driver.implicitly_wait(10)

    # Megnézzük, megjelent-e a div elemünk
    success_message = driver.find_element(By.XPATH,"//div[@class='success-message']")
    if success_message.is_displayed():
        print("Sikerült az űrlap küldése!")
    else:
        print("Nem sikerült az űrlap küldése!")

    # Csukjuk be a böngésző ablakot!
    driver.quit()
