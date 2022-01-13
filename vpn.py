import time
import yaml
from selenium import webdriver


def read_yaml(path):
    with open(path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


# Change here according to your environment
VPN_INFO = ""  # Enter info.yaml path
USERNAME = ""  # Enter username
DRIVER = ""  # Enter chromedriver path

# Read vpn info
info = read_yaml(VPN_INFO)
print(info)

# Open chrome
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir=/Users/{USERNAME}/Library/Application Support/Google/Chrome/Profile 1")
driver = webdriver.Chrome(DRIVER, options=options)
driver.get("https://vpn.korea.ac.kr")

# Login vpn
driver.find_element_by_name('username').send_keys(info['id'])
driver.find_element_by_name('-meaningless-').click()
driver.find_element_by_name('password').send_keys(info['pw'])
driver.find_element_by_xpath('//*[@id="field-submit"]').click()

# Close session
time.sleep(10)
driver.quit()

print("Execute vpn")
