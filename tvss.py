import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC1
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080");
chrome_options.add_argument("--start-maximized");
chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options) # change as per your location for your driver (chrome,phantomjs,webkit,firefox)
driver.get ("xx.com") # set your chart sharing setting to public, and put the link here
wait_time = 30 # a very long wait time
time.sleep(20)
ActionChains(driver).key_down(Keys.ALT).send_keys('s').perform()
element = WebDriverWait(driver, wait_time).until(EC1.element_to_be_clickable((By.LINK_TEXT, 'Save image')))
element.click()
time.sleep(3)
# new_name = time.strftime("%Y-%m-%d_%H%M%S") + ".png"
# dest_dir = ""
# current_file_name = ""
# os.rename(current_file_name, dest_dir+"/"+new_name)
driver.close()
driver.quit()
