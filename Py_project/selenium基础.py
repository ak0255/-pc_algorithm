from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()
web.get("http://lagou.com")

# 找到北京地区，并点击
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a')
el.click()

time.sleep(1)

web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python", Keys.ENTER)

li_lists = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')

# print(li_lists)
# print(type(li_lists))

for li in li_lists :
    job_name = li.find_element_by_tag_name('h3').text
    job_price = li.find_element_by_xpath('./div/div/div[2]/div/span').text
    company_name = li.find_element_by_xpath('./div/div[2]/div/a').text
    print(company_name, job_name, job_price)
    pass