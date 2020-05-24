from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')
browser.maximize_window()
browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
button_text = browser.find_element_by_class_name('btn-default')
user_message = browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('hello folks')
button_text.click()

