from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import allure
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


# driver = webdriver.Firefox()  # 初始化对象
# action = ActionChains(driver)
# driver.get("https://www.12306.cn/index/")
# ###出发地输入###
# Departure = driver.find_element(By.CSS_SELECTOR,"html body div#toolbar_Div div.section-first div.search-index div.search-main div.search-main-item div.search-main-tab div.search-tab-bd div.search-tab-item div.search-form div.form-item-group div.form-item div.form-bd div.input-box.input-city input#fromStationText.input")
# action.move_to_element(Departure).click().perform()
# Departure.send_keys("北京")
# # # 下拉框移动到北京
# SEl = driver.find_element(By.XPATH,'//*[@id="citem_2"]')
# action.move_to_element(SEl).click().perform()
# time.sleep(2)
# ###目的地地输入###
# destination = driver.find_element(By.XPATH,"//*[@id='toStationText']")
# action.move_to_element(destination).click().perform()
# destination.send_keys("上海")
# DEL = driver.find_element(By.XPATH,'//*[@id="citem_2"]')
# action.move_to_element(DEL).click().perform()
# ###处理只读控件时间，并输入时间##
# date_txt = driver.find_element(By.XPATH,"//*[@id='train_date']")
# # 方法1：通过js的getElementById去掉只读属性
# driver.execute_script("document.getElementById('train_date').removeAttribute('readonly');")
# # # 方法2：通过js的document.arguments[0]去掉只读属性
# # driver.execute_script("arguments[0].removeAttribute('readonly');",date_txt)
# # 通过send_keys操作，重新写值
# date_txt.clear()   # 先清除原来的日期值
# date_txt.send_keys('2024-04-01')
# ###页面滑动
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.execute_script("window.scrollTo(0,0)")
# ###执行查询操作
# research = driver.find_element(By.XPATH,'//*[@id="search_one"]')
# action.move_to_element(research).click().perform()
# driver.implicitly_wait(2)
# ###异常截图
# driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\double.png")
# ##实现文件上传功能
# driver.get("https://www.baidu.com")
# paten = driver.find_element(By.XPATH,"//span[@class='soutu-btn']")
# action.move_to_element(paten).click().perform()
# time.sleep(6)
# driver.find_element(By.CSS_SELECTOR,".upload-pic").send_keys("C:\\Users\\Administrator\\Desktop\\1.PNG")
#
# ###PageObject##
class SearchPage:
    __INPUT_SEARCH_DEPATURE_CITY = (By.XPATH, "//*[@id='fromStationText']")
    __INPUT_SEARCH_DESTINATION_CITY = (By.XPATH, "//*[@id='toStationText']")
    __INPUT_SEl = (By.XPATH, "//*[@id='citem_2']")
    __BUTTON_SEARCH = (By.XPATH, '//*[@id="search_one"]')

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.action = ActionChains(self.driver)
        self.driver.implicitly_wait(3)
        self.driver.get("https://www.12306.cn/index")
        time.sleep(2)

    def search_stock(self, depart_city: str, destination_city: str):
        ### Input departure
        Scity = self.driver.find_element(*self.__INPUT_SEARCH_DEPATURE_CITY)
        self.action.move_to_element(Scity).click().perform()
        Scity.send_keys(depart_city)
        self.action.move_to_element(self.driver.find_element(*self.__INPUT_SEl)).click().perform()
        ## Input destination city
        Dcity = self.driver.find_element(*self.__INPUT_SEARCH_DESTINATION_CITY)
        self.action.move_to_element(Dcity).click().perform()
        Dcity.send_keys(destination_city)
        time.sleep(1)
        self.action.move_to_element(self.driver.find_element(*self.__INPUT_SEl)).click().perform()
        self.action.move_to_element(self.driver.find_element(*self.__BUTTON_SEARCH)).click().perform()


PO = SearchPage().search_stock("北京","上海")