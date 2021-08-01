from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html")
    time.sleep(3)

    # TC1: Teszteld le, hogy betöltés után megjelennek filmek az alkalmazásban, méghozzá 24 db.

    movies_number = driver.find_elements_by_class_name("container-movies")
    print(len(movies_number))
    assert len(movies_number) == 24

    # TC2: Teszteld le, hogy fel lehet-e venni az alábbi adatokkal egy új filmet

    # a kikeresendő mezők id-jét és a tesztadatokat listába gyűjtjük, és egy definiált függvényt for ciklussal meghívunk annyiszor, ahány tesztadatunk van
    ids = ["nomeFilme", "anoLancamentoFilme", "anoCronologiaFilme", "linkTrailerFilme", "linkImagemFilme",
           "linkImdbFilme"]
    test_data = ["Black widow", "2021", "2020", "https://www.youtube.com/watch?v=Fp9pNPdNwjI",
                 "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg",
                 "https://www.imdb.com/title/tt3480822/"]

    register_button = driver.find_element_by_class_name("mostra-container-cadastro")
    register_button.click()
    time.sleep(2)


    def find_and_send(id, data):
        driver.find_element_by_id(id).send_keys(data)


    for i in range(len(test_data)):
        find_and_send(ids[i], test_data[i])

    save_button = driver.find_element_by_xpath("/html/body/div[2]/div[2]/fieldset/button[1]")
    save_button.click()

    movies_number_after_new_reg = driver.find_elements_by_class_name("container-movies")
    print(len(movies_number_after_new_reg))
    assert len(movies_number_after_new_reg) == 25

    time.sleep(2)

finally:
    driver.close()
