from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('./chromedriver')

def getAIAdata(birth, gender):
    driver.get('https://www.aia.co.kr/ko/our-products/medical-protection/non-par-denteal-health-plan.html')
    # -----logic 작성----
    textBox = driver.find_element_by_xpath('//*[@id="aia644363719"]')
    textBox.send_keys("19"+birth)

    if gender == 1:
        femaleBtn = driver.find_element_by_xpath(
            '//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]')
        # '//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]
        femaleBtn.click()
    else:
        maleBtn = driver.find_element_by_xpath(
            '//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[2]')
        maleBtn.click()

    resultBtn = driver.find_element_by_xpath('//*[@id="btn806817556"]')
    resultBtn.click()
    driver.implicitly_wait(3)
    price = driver.find_element_by_xpath(
        '//*[@id="premium-by-timespan-value"]').text
    print(price)
    tableBody = driver.find_element_by_xpath(
        '//*[@id="collapse-large-724022276"]/div[1]/div/table').find_element_by_tag_name('tbody')
    driver.find_element_by_xpath(
        '//*[@id="the_fine_print"]/div[2]/div[1]/div[2]/div/a[2]').click()
    rows = tableBody.find_elements_by_tag_name("tr")
    contentsList = []

    for index, value in enumerate(rows):
        if index != 0:
            print(value.find_elements_by_tag_name('td')[0].text)
            contentsList.append(value.find_elements_by_tag_name('td')[0].text)

getAIAdata('890119', 0)