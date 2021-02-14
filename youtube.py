from selenium import webdriver
a='C:/Users/fdm19/Downloads/chromedriver.exe'
driver = webdriver.Chrome(executable_path=a)
driver.get('https://www.youtube.com/')
elem1=driver.find_element_by_xpath('//input[@id=\'search\']')
elem1.send_keys('sasageyo')
elem2=driver.find_element_by_xpath('//button[@id=\'search-icon-legacy\']')
elem2.click()