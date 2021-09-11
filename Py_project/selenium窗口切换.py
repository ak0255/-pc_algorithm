from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()
web.get('http://lagou.com')

web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a').click()

time.sleep(1)

web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)

'''
li_lists = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')

for li in li_lists :
    job_name = li.find_element_by_tag_name('h3').text
    job_price = li.find_element_by_xpath('./div/div/div[2]/div/span').text
    job_need = li.find_element_by_xpath('./div/div/div[2]/div').text
    company_name = li.find_element_by_xpath('./div/div[2]/div/a').text
    print(job_name, job_price, job_need, company_name)
    pass
'''

time.sleep(2)
web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[2]/div[1]/div[1]/div[1]/a/h3').click()
web.switch_to_window(web.window_handles[-1])

job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)
web.close()

web.switch_to_window(web.window_handles[0])
name = web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[2]/div[1]/div[1]/div[1]/a/h3').text
print(name)
