import mock
import pytest
from src.single_label_scraper import get_search_inputs, clean_text


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
