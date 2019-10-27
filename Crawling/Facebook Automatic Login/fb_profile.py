from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# replace with your FB credentials
user = "id"
pwd = "password"

# accessing FB
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://facebook.com/")
assert "Facebook" in driver.title

# login to FB
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

# accessing personal profile using xpath
a = driver.find_elements_by_xpath('//*[@id="u_0_a"]/div[1]/div[1]/div/a')
driver.get(a[0].get_attribute('href'))

req = driver.page_source

# parsing with bs4
soup = BeautifulSoup(req, 'html.parser')

# load personal profile
information_list = soup.select('#intro_container_id')
for information in information_list:
    print(information.text)
