
# http://www.eum.go.kr/web/am/amMain.jsp	#
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.eum.go.kr/web/am/amMain.jsp")


# addressInput = driver.find_element_by_xpath('//*[@id="recent"]/input')
# addressInput.send_keys('서울시 서대문구 거북골로18가길 23')
# nextButton = driver.find_element_by_xpath(
#     '//*[@id="frm"]/fieldset/div[3]/p/span/a')
# nextButton.click()

sidoSelect = Select(driver.find_element_by_xpath('//*[@id="selSido"]'))
sidoSelect.select_by_visible_text('경기도')

