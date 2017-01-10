import time
import tweepy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

key = "o5lfqT90lF9eaiXrikXXdw2o0"
secret = "8HplZfUMPmZ0yHIdtWdLeLy3FWODfyWTuOu6yA55DGEc8dE5YK"
accessToken = "809565371695034368-WoO437rm0eFuPIRx9LpyE90RTMfU7Dv"
accessSecret = "QR8GN5yWWcUn7FDvMvrVAX093clDrv1ls41lcoLmvzyj1"

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(accessToken, accessSecret)

api = tweepy.API(auth)


driver = webdriver.Chrome()
page = driver.get("https://www.measurementlab.net/p/ndt-ws.html#test")
time.sleep(2)
button = driver.find_element_by_css_selector('.start')
button.click()
try:
    test = WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.ID, "upload-speed")))
except:
    driver.quit()
uploadNum = driver.find_element_by_id('upload-speed').text
uploadType = driver.find_element_by_id('upload-speed-units').text
dlNum = driver.find_element_by_id('download-speed').text
dlType = driver.find_element_by_id('download-speed-units').text

mySpeed = 45
print (time.strftime("%H:%M:%S"), print (time.strftime("%d/%m/%Y")))
def convertMeasurement(speed, type):
    if str(speed) == "NAN":
        return "The result was null"
    elif str(type) == "kb/s":
        speed = float(speed.text)/100
        return speed
    else:
        return speed

upload = convertMeasurement(uploadNum, uploadType)
download = convertMeasurement(dlNum, dlType)
if str(download) == "The result was null":
    api.update_status("@AustinDoesStuff, it didn't work.")
    exit()
if mySpeed* .8 > float(download):
    api.update_status("@AustinDoesStuff " + str(download) + " Mb/s down, and " + str(upload) + " Mb/s up")
else:
    api.update_status("@AustinDoesStuff This is acceptable")
