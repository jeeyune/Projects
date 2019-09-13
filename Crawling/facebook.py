from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

user = "oingoing_@naver.com"
pwd = "oingoing77"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://facebook.com/")
assert "Facebook" in driver.title

elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
