import mock
import pytest
from src.app import get_search_inputs


def test_get_search_inputs():
    """It should return a string"""
    result1, result2 = get_search_inputs(
        "ash tree, ash tree fall , ash tree winter, ash tree spring, ash tree summer"
    )
    assert result1 == "ash tree"
    assert result2 == [" ash tree fall ", " ash tree winter", " ash tree spring", "ash tree summer"]
