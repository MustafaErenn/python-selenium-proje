from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get("https://www.instagram.com")
time.sleep(10)

userName = browser.find_element_by_name("username")

password = browser.find_element_by_name("password")

userName.send_keys("username")#username yerine kendi instagram kullanici adinizi giriniz
password.send_keys("password")#password yerine kendi instagram sifrenizi giriniz

# giris yap buton xpath ===== //*[@id="loginForm"]/div/div[3]/button

login = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
login.click()

time.sleep(10)
#search  == //*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input

search = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
search.send_keys("deneme")#deneme yerine gondermek istediginiz kisinin kullanici adini giriniz

time.sleep(10)

#searchButton = "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div/div[1]"

searchButton = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div/div[1]")
searchButton.click()

time.sleep(10)

# send message = //*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button
sendMessage = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")
sendMessage.click()

time.sleep(10)

#dm == //*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea

dm = browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
dm.send_keys("deneme mesaji")#gondermek istediginiz mesaji buraya giriniz
time.sleep(10)

# dm sending == //*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button

sendDmButton = browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
sendDmButton.click()
time.sleep(10)


browser.close()