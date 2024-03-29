import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver_fun(request):
    """ Initialized UDPCP class """
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.get("https://xueqiu.com/")
    time.sleep(2)
    return driver

@pytest.fixture(params=["阿里巴巴"])
def parame_stock(request):
    return request.param


@pytest.mark.usefixtures("driver_fun","parame_stock")
class TestSearchPage(object):

    __INPUT = (By.NAME, "q")
    __SEARCH = (By.CSS_SELECTOR, ".index_iconfont_mYK")


    def test_search_stock(self,driver_fun,parame_stock):
        stock_name = parame_stock
        driver_fun.find_element(*self.__INPUT).send_keys(stock_name)
        driver_fun.find_element(*self.__SEARCH).click()
