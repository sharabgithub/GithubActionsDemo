from selenium import webdriver
#---------------------------------------------------
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#----------------------------------------------------
from selenium.webdriver.common.alert import Alert
#---------------------------------------------------
from selenium.webdriver.common.action_chains import ActionChains
#---------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#--------------------------------------------------
from selenium.webdriver.chrome.options import Options
#---------------------------------------------------
import time
#-----------------------------------------------------
from selenium.webdriver.support.relative_locator import with_tag_name
from selenium.webdriver.support.relative_locator import locate_with

opts = Options()
opts.add_argument("--start-maximized")
opts.add_argument("--window-size=1920,1080")
opts.add_argument("--no-sandbox")
opts.page_load_strategy = "normal"

dr = webdriver.Chrome(options=opts)
dr.maximize_window()

# dr.implicitly_wait(20)
wait = WebDriverWait(dr, 30)

alert = Alert(dr)

dr.get("https://testautomationpractice.blogspot.com/")
name_ele = dr.find_element(By.XPATH, "//input[@id='name']")
email_ele = dr.find_element(locate_with(By.TAG_NAME,"input").below(name_ele))
address_ele = dr.find_element(By.ID, "textarea")
ph_ele = dr.find_element(locate_with(By.ID, "phone").above(address_ele))

name_ele.send_keys("Prasanna")
email_ele.send_keys("email@abc.com")
ph_ele.send_keys("1900889988")
address_ele.send_keys("Bengaluru, Karnataka")

dr.execute_script("window.scrollBy(0, 1000);")
time.sleep(5)
dr.find_element(By.CSS_SELECTOR, ".submit-btn")
time.sleep(2)
dr.execute_script("window.scrollBy(0, -800);")
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='alertBtn']"))).click()
# dr.find_element(By.XPATH, "//button[@id='alertBtn']")
time.sleep(2)
alert.accept()
time.sleep(2)