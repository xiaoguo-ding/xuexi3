from selenium import webdriver
from common.base import Base

def test_guge():
    driver = webdriver.Chrome()
    web = Base(driver)  # 实例化
    driver.get("https://www.baidu.com")
    loc_1 = ("id", "kw")
    web.send(loc_1, "hello")
    loc_2 = ("id", "su")
    web.click(loc_2)

    # Python is likely shutting down
    '''driver.close()'''