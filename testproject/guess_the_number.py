from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html")
    time.sleep(2)

    # TC1 : találgatás
    # függvénnyel visszük be az újabb számokat, és for ciklussal iterálunk amíg nincs meg a keresett szám, ezt a végén ellenőrizzük

    input_number = driver.find_element_by_xpath("/html/body/div/div[2]/input")
    guess_button = driver.find_element_by_xpath("/html/body/div/div[2]/span/button")
    message = driver.find_element_by_xpath("/html/body/div/p[5]")
    message_down = driver.find_element_by_xpath("/html/body/div/p[4]")
    message_up = driver.find_element_by_xpath("/html/body/div/p[3]")
    number_of_guesses = driver.find_element_by_xpath("/html/body/div/div[3]/p/span").text


    def send_new_number(num):
        input_number.clear()
        input_number.send_keys(num)
        guess_button.click()


    for i in range(1, 101):
        send_new_number(i)
        if message.text == "Yes! That is it.":
            break
            # print(i)
            # print(type(i))
            # print(number_of_guesses)
            # print(type(number_of_guesses))
            assert number_of_guesses == i + 1

    # TC2 : intervallumon kívüli számok (-19 és 255)
    # a definiált függvénnyel meghívjuk a két vizsgálanó számra is, és ellenőrizzük a szöveget
    send_new_number(-19)
    assert message_down.text == "Guess higher."

    send_new_number(255)
    assert message_up.text == "Guess lower."

    time.sleep(2)

finally:
    driver.close()