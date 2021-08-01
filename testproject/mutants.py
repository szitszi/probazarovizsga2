from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html")
    time.sleep(1)

    original_group = driver.find_element_by_xpath("/html/body/div/label[1]")
    x_force = driver.find_element_by_xpath("/html/body/div/label[2]")
    x_factor = driver.find_element_by_xpath("/html/body/div/label[3]")
    hellfire = driver.find_element_by_xpath("/html/body/div/label[4]")

    # TC1: iceman ellenőrzése

    iceman = driver.find_element_by_xpath('//*[@id="iceman"]/h2')
    original_group.click()
    assert iceman.is_displayed()
    x_factor.click()
    assert iceman.is_displayed()
    x_force.click()
    assert not iceman.is_displayed()
    hellfire.click()
    assert not iceman.is_displayed()

    time.sleep(2)

finally:
    driver.close()