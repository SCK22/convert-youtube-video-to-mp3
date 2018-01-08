#Load the requiredlibraries
from selenium import  webdriver
from selenium import  *
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#prompot the user for the link of the video to be convereted
video_to_be_converted = input("Please provide the youtube url of the song you want to download as mp3: ")
driver = webdriver.Chrome("path to chromedriver") # set the chrome webdriver
driver.get("https://www.mp3converter.net/")
# Find the "enter url" element 
if driver.find_element_by_xpath("//*[@id=\"videoURL\"]"):
    print("Opened the site successfully")
    youtube_link_element = driver.find_element_by_xpath("//*[@id=\"videoURL\"]")
    youtube_link_element.send_keys(str(video_to_be_converted))
    youtube_link_element.send_keys(Keys.RETURN)
delay = 100
successful_conversion_element = "//*[@id=\"conversionSuccess\"]/p[4]/a"
# try:
#     element = 
# WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,successful_conversion_element)))
time.sleep(10)
if driver.find_element_by_xpath(successful_conversion_element):
        print("Converting the video")
        enter_to_download = driver.find_element_by_xpath(successful_conversion_element)
        enter_to_download.send_keys(Keys.RETURN)
        print("Video Converted")
        state = 1
else:
    print("took too long")
    state = 0
#     WebDriverWait(driver=driver,delay)
if state ==1:
    time.sleep(10)
    driver.quit()
