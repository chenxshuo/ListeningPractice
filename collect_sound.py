from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import *
from time import sleep
import os


def set_profile():
    profile = webdriver.FirefoxProfile(
        "C:/Users/chenxshuo/Desktop/GermanNumber/firefox profile"
    )
    # set socks5
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", "127.0.0.1")
    profile.set_preference("network.proxy.socks_port", 7890)
    profile.set_preference("network.proxy.socks_version", 5)

    profile.set_preference(
        "browser.download.dir", "C:/Users/chenxshuo/Desktop/GermanNumber/"
    )
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/mp3")

    profile.update_preferences()
    return profile


def change_name(i):
    download_dir = "C:/Users/chenxshuo/Downloads/"
    mp3_files = []
    files = os.listdir(download_dir)
    for file in files:
        if file.find("ttsMP3") is not -1:
            mp3_files.append(file)
    mp3_file = mp3_files[0]
    os.rename(download_dir + mp3_file, download_dir + str(i) + ".mp3")


def download_sounds():
    prof = set_profile()
    driver = webdriver.Firefox(
        executable_path="C:/Users/chenxshuo/Desktop/GermanNumber/geckodriver",
        firefox_profile=prof,
    )
    driver.get("https://ttsmp3.com/text-to-speech/German/")

    for i in range(0, 999):
        driver.find_element_by_xpath("//*[@id='voicetext']").send_keys(str(i))
        sleep(1)
        driver.find_element_by_xpath("//*[@id='downloadenbutton']").click()
        sleep(1)
        driver.find_element_by_xpath("//*[@id='voicetext']").clear()
        sleep(1)
        change_name(i)


if __name__ == "__main__":
    download_sounds()
