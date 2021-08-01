from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html")
    time.sleep(3)

    # TC1:
    with open("data.txt", "r") as f:
        result = f.read()
    print(type(result))
    # print(result)

    list_of_elements = driver.find_elements_by_xpath("/html/body/div/ul/li")
    # print(len(list_of_elements))

    nr_raw = []
    for elem in list_of_elements:
        nr_raw.append(elem.get_attribute("data-pos"))
    print(nr_raw)

    nr = []
    for el in nr_raw:
        if el != None:
            nr.append(el)
    print(nr)
    print(len(nr))

    name_of_elements = driver.find_elements_by_xpath("/html/body/div/ul/li/span")

    print(len(name_of_elements))

    names = []
    for name in name_of_elements:
        names.append(name.text)
    print((names))

    for i in range(len(nr)):
        check_list = []
        # check_list = nr[i] + ' ,' + names[i] + '\n'
    print(check_list)

    # assert check_list == result

    time.sleep(2)

finally:
    driver.close()
