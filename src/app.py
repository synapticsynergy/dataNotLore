# Python program to scrape website
import requests
import csv
import sys
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

file_path = os.path.dirname(os.path.abspath(__file__))
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")


def main(annotation, search_terms):
    """
    Pass in the annotation and search terms, and get a list of image urls in csv with the annotation in the filename.
    """
    root_path = file_path.split("/")[0:-1]
    csv_filename = annotation.replace(" ", "_")
    output_dir = os.path.join("/".join(root_path), "data", f"{csv_filename}.csv")
    if os.path.exists(output_dir):
        os.remove(output_dir)
    for search_term in search_terms:
        print(f"Searching: {search_term}")
        url = f"https://www.google.com/imghp?q={search_term}"
        chromedriver_path = os.path.join("/".join(root_path), "bin", "chromedriver")
        browser = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=option)
        browser.get(url)
        search_button = browser.find_element_by_xpath("//button[@aria-label='Google Search']")
        search_button.click()
        get_image_urls(annotation, browser, output_dir, csv_filename)


def get_image_urls(annotation, browser, output_dir, csv_filename):
    urls = browser.execute_script(
        "urls = Array.from(document.querySelectorAll('.rg_di .rg_meta')).map(el=>JSON.parse(el.textContent).ou); return urls;"
    )
    csv_format = ",\n".join(urls)
    file = open(output_dir, "a")
    file.write(csv_format)
    file.close()
    print(f"Wrote Image urls to {csv_filename}.csv")
    sleep(5)
    browser.quit()


if __name__ == "__main__":
    annotation = "ash tree"
    main(annotation, ["ash tree fall", "ash tree winter", "ash tree spring", "ash tree summer"])
