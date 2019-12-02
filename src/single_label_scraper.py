# Python program to scrape website
import csv
import sys
import os
from sys import platform
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
option.add_argument("--start-maximized")


def scrape_images(annotations="annotations", num_images=200):
    annotations_csv = os.path.join(
        "/".join(root_path), "src", "annotations", f"{annotations}.csv"
    )
    with open(annotations_csv, "r") as file:
        csv_rows = file.readlines()
        for row in csv_rows:
            annotation, search_terms = get_search_inputs(row)
            print(annotation, search_terms)
            request_search_terms(annotation, search_terms, num_images)


def get_os_platform():
    os_driver_dir = {"linux": "linux", "linux2": "linux", "darwin": "mac"}
    return os_driver_dir[platform]


def get_search_inputs(row):
    cells = row.split(",")
    annotation = cells[0]
    if len(cells) is 1 or cells[1] is "".strip(" \u200e\t\n\r"):
        cleaned_annotation, cleaned_search_terms = clean_text(annotation, [annotation])
        return cleaned_annotation, cleaned_search_terms
    search_terms = cells[1:]
    cleaned_annotation, cleaned_search_terms = clean_text(annotation, search_terms)
    return cleaned_annotation, cleaned_search_terms


def clean_text(annotation, row):
    cleaned_annotation = annotation.strip(" \u200e\t\n\r")
    print(len(cleaned_annotation))
    print(len("ash tree"))
    mapped_search_terms = map(lambda x: x.strip(" \u200e\t\n\r"), row)
    cleaned_search_terms = [term for term in mapped_search_terms if term]
    return cleaned_annotation, cleaned_search_terms


def request_search_terms(annotation, search_terms, num_images):
    """
    Pass in the annotation and search terms, and get a list of image urls in csv with the annotation in the filename.
    """
    annotation = annotation.replace(" ", "_")
    data_dir = os.path.join("/".join(root_path), "data_csv")
    output_dir = os.path.join("/".join(root_path), "data_csv", annotation)
    output_file_path = os.path.join(
        "/".join(root_path), "data_csv", annotation, f"{annotation}.csv"
    )
    prepare_clean_run(data_dir, output_dir, output_file_path)
    scrape_google(search_terms, annotation, output_file_path, num_images)


def scrape_google(search_terms, annotation, output_file_path, num_images):
    for search_term in search_terms:
        trimmed_search_term = search_term.strip(" \u200e\t\n\r")
        print(f"Searching: {trimmed_search_term}")
        url = f"https://www.google.com/imghp?q={trimmed_search_term}"
        chromedriver_path = os.path.join(
            "/".join(root_path), "bin", get_os_platform(), "chromedriver"
        )
        browser = webdriver.Chrome(
            executable_path=chromedriver_path, chrome_options=option
        )
        browser.get(url)
        search_button = browser.find_element_by_xpath(
            "//button[@aria-label='Google Search']"
        )
        search_button.click()
        write_images_csv(browser, output_file_path, annotation, num_images)


def prepare_clean_run(data_dir, output_dir, output_file_path):
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    if os.path.exists(output_file_path):
        os.remove(output_file_path)


def write_images_csv(browser, output_dir, csv_filename, num_images):
    urls = get_image_urls(browser, num_images)
    csv_format = "\n".join(urls)
    file = open(output_dir, "a")
    file.write(csv_format)
    file.close()
    print(f"Wrote Image urls to {csv_filename}.csv")
    sleep(4)
    browser.quit()


def get_image_urls(browser, num_images):
    browser.implicitly_wait(5)
    images_per_page = 100
    max_scrapable_images = 400
    remaining_images = num_images - images_per_page
    while remaining_images > 0:
        print(remaining_images)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        browser.implicitly_wait(5)
        sleep(3)
        if remaining_images % max_scrapable_images == 0:
            print(remaining_images % max_scrapable_images, ' hit condition')
            search_button = browser.find_element_by_xpath(
                "//input[@value='Show more results']"
            )
            browser.implicitly_wait(5)
            try:
                search_button.click()
                browser.implicitly_wait(5)
            except Exception:
                print('Probably reached end of results')
                pass
        remaining_images = remaining_images - images_per_page
    sleep(5)
    urls = browser.execute_script(
        "urls = Array.from(document.querySelectorAll('.rg_di .rg_meta')).map(el=>JSON.parse(el.textContent).ou); return urls;"
    )
    browser.implicitly_wait(5)
    print(len(urls),'length at end')
    sleep(5)
    return urls


# if __name__ == "__main__":
    # scrape_images(num_images=200)
    # annotation = "ash tree"
    # request_search_terms(
    #     annotation, ["ash tree fall", "ash tree winter", "ash tree spring", "ash tree summer"]
    # )
