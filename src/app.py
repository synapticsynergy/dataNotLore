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
root_path = file_path.split("/")[0:-1]
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")


def main():
    annotations_csv = os.path.join("/".join(root_path), "src", "annotations", "annotations.csv")
    with open(annotations_csv, "r") as file:
        csv_rows = file.readlines()
        for row in csv_rows:
            cells = row.split(",")
            annotation = cells[0]
            search_terms = cells[1:]
            search_terms[-1] = search_terms[-1].strip(" \t\n\r")
            print(annotation, search_terms)
            request_search_terms(annotation, search_terms)


def request_search_terms(annotation, search_terms):
    """
    Pass in the annotation and search terms, and get a list of image urls in csv with the annotation in the filename.
    """
    csv_filename = annotation.replace(" ", "_")
    output_dir = os.path.join("/".join(root_path), "data", f"{csv_filename}.csv")
    if os.path.exists(output_dir):
        os.remove(output_dir)
    for search_term in search_terms:
        trimmed_search_term = search_term.strip(" \t\n\r")
        print(f"Searching: {trimmed_search_term}")
        url = f"https://www.google.com/imghp?q={trimmed_search_term}"
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
    csv_format = "\n".join(urls)
    file = open(output_dir, "a")
    file.write(csv_format)
    file.close()
    print(f"Wrote Image urls to {csv_filename}.csv")
    sleep(5)
    browser.quit()


if __name__ == "__main__":
    main()
    # annotation = "ash tree"
    # request_search_terms(
    #     annotation, ["ash tree fall", "ash tree winter", "ash tree spring", "ash tree summer"]
    # )
