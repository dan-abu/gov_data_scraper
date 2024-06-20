"""Automates downloading a file by opening up a website and clicking the download buttong"""
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_file_suffix(file_path: str) -> tuple:
    """Returns file's root (e.g. /home/User/Desktop/file) and its ext (e.g. .txt)"""
    root, suffix = os.path.splitext(file_path)
    return (root, suffix)


def webscraper(website_url: str, xpath: str, downloadDir: str) -> None:
    """Download file to preferred download folder
    from website using website's download click button"""
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": downloadDir}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chromeOptions)
    try:
        driver.get(website_url)
        wait = WebDriverWait(driver, 10)
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        download_button.click()
        time.sleep(5)
    except Exception as e:
        print("Unable to download file.")
        print(e)
        raise e
    else:
        new_file = os.listdir(downloadDir)[0]
        print(f"Successfully downloaded file {new_file}.")
    finally:
        driver.quit()


if __name__ == "__main__":
    url = sys.argv[1]
    xpath = sys.argv[2]
    downloadDir = sys.argv[3]
    webscraper(url, xpath, downloadDir)
