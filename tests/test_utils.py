from common.utils import parse_csv_to_dicts, sort_records
from tests.data.expected_parsed_records import EXPECTED_PARSED_RECORDS, EXPECTED_SORTED_PARSED_RECORDS

import pytest


TEST_DATA = "tests/data/test_dataset.csv"


def test_parse_csv_to_dicts():
    """Tests that parse_csv_to_dicts produces
    the expected parsed list of dicts"""
    pytest.raises(FileNotFoundError, parse_csv_to_dicts, "data3.csv")
    assert parse_csv_to_dicts(TEST_DATA) == EXPECTED_PARSED_RECORDS

def test_sort_records():
    """ Tests the expected behaviour of the 
    sort_records function"""
    sorted_records = sort_records(EXPECTED_PARSED_RECORDS, by="Current Rent")
    assert sorted_records == EXPECTED_SORTED_PARSED_RECORDS
