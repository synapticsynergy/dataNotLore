import mock
import pytest
import os
from src.single_label_scraper import get_search_inputs, clean_text, get_os_platform, get_image_urls
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


def scrape_google_util(search_term):
    """Test utility function"""
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
    return browser


def test_get_search_inputs():
    """It should return a string for annotation label and an array for search terms"""
    result1, result2 = get_search_inputs(
        "ash tree, ash tree fall , ash tree winter, ash tree spring, ash tree summer"
    )
    assert result1 == "ash tree"
    assert result2 == ["ash tree fall", "ash tree winter", "ash tree spring", "ash tree summer"]


def test_get_search_inputs2():
    """It should return a string and an array with one item if only one column is found"""
    result1, result2 = get_search_inputs(
        "ash tree"
    )
    assert result1 == "ash tree"
    assert result2 == ["ash tree"]


def test_clean_text():
    """It should remove invalid search terms and unwanted characters"""
    result1, result2 = clean_text(
        " ash tree ", [" ash tree ",""," ","\n"]
    )
    assert result1 == "ash tree"
    assert result2 == ["ash tree"]


def test_get_image_urls():
    """It should return 100 images"""
    browser = scrape_google_util('ash tree')
    browser.implicitly_wait(5)
    result = get_image_urls(browser, 100)
    browser.close()
    assert len(result) == 100


def test_get_image_urls2():
    """It should return 300 images"""
    browser = scrape_google_util('ash tree')
    browser.implicitly_wait(5)
    result = get_image_urls(browser, 2000)
    browser.close()
    print(len(result), ' this is how many images were printed')
    assert len(list(set(result))) > 600
