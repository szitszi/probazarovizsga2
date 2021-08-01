from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")
    time.sleep(2)

    test_data_g = ['8', '2021.08.01.', 'Midday', '4', 'John Doe', 'jdoe@test.com', 'example text']
    expected_message = "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."


    # TC1 : formanyomtatvány ellenőrzés

    select_field_1 = Select(driver.find_element_by_name('bf_totalGuests'))
    select_field_1.select_by_visible_text(test_data_g[0])
    next_button_1 = driver.find_element_by_xpath("//*[@id='step1']/ul/li[2]/button")
    next_button_1.click()
    date_field = driver.find_element_by_xpath("//*[@id='step2']/ul/li[1]/input")
    date_field.send_keys(test_data_g[1])
    select_field_2 = Select(driver.find_element_by_name('bf_time'))
    select_field_2.select_by_visible_text(test_data_g[2])
    select_field_3 = Select(driver.find_element_by_name('bf_hours'))
    select_field_3.select_by_visible_text(test_data_g[3])
    next_button_2 = driver.find_element_by_xpath("//*[@id='step2']/ul/li[4]/button")
    next_button_2.click()
    name_field = driver.find_element_by_xpath("//*[@id='step3']/ul/li[1]/input")
    name_field.send_keys(test_data_g[4])
    email_field = driver.find_element_by_xpath("//*[@id='step3']/ul/li[2]/input")
    email_field.send_keys(test_data_g[5])
    extra_field = driver.find_element_by_xpath("//*[@id='step3']/ul/li[3]/textarea")
    extra_field.send_keys(test_data_g[6])
    request_send_button = driver.find_element_by_xpath("//*[@id='step3']/ul/li[4]/button")
    request_send_button.click()
    time.sleep(4)
    message = driver.find_element_by_xpath("//*[@id='booking-form']/h2").text

    assert message == expected_message

    # TC2 : email ellenőrzés
    driver.refresh()
    time.sleep(2)
    test_data_w1 = ['8', '2021.08.01.', 'Midday', '4', 'John Doe', 'jdoetest.com', 'example text']
    test_data_w2 = ['8', '2021.08.01.', 'Midday', '4', 'John Doe', 'jdoetest@', 'example text']

    select_field_1 = Select(driver.find_element_by_name('bf_totalGuests'))
    select_field_1.select_by_visible_text(test_data_w1[0])
    next_button_1 = driver.find_element_by_xpath("//*[@id='step1']/ul/li[2]/button")
    next_button_1.click()
    date_field = driver.find_element_by_xpath("//*[@id='step2']/ul/li[1]/input")
    date_field.send_keys(test_data_w1[1])
    select_field_2 = Select(driver.find_element_by_name('bf_time'))
    select_field_2.select_by_visible_text(test_data_w1[2])
    select_field_3 = Select(driver.find_element_by_name('bf_hours'))
    select_field_3.select_by_visible_text(test_data_w1[3])
    next_button_2 = driver.find_element_by_xpath("//*[@id='step2']/ul/li[4]/button")
    next_button_2.click()
    name_field = driver.find_element_by_xpath("//*[@id='step3']/ul/li[1]/input")
    name_field.send_keys(test_data_w1[4])
    email_field = driver.find_element_by_xpath("//*[@id='step3']/ul/li[2]/input")
    email_field.send_keys(test_data_w1[5])
    time.sleep(2)
    # error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "bf_email-error"))).text
    error = driver.find_element_by_id("bf_email-error").text
    print(error)
    #
    # assert msg is not None
    # assert msg == "PLEASE ENTER A VALID EMAIL ADDRESS."



    time.sleep(1)

finally:
    driver.close()