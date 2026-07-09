from typing import Tuple

import pytest

from techtask import PASSING_TESTS
from techtask.app import Record, get_male_count, csv_to_records


def test_01_can_count_number_of_males():
    """
    Count of the number of males in the rows of data from
    the provided records object below by changing the logic in the function
    get_male_count() found in app.py
    """

    records = [
        Record(first_name="mitchell", surname="clausson", dob="21/01/1980", sex="m"),
        Record(first_name="thomas", surname="skindstad", dob="18/06/1988", sex="m"),
        Record(first_name="susan", surname="boyle", dob="01/04/1961", sex="f"),
    ]

    actual_value_1 = get_male_count(records)

    assert actual_value_1 == 2

    # Remove this comment to go to the next test


@pytest.mark.skipif(PASSING_TESTS < 1, reason="You need to finish the first test!")
def test_02_load_some_data():
    """
    This test is to show that you are comfortable loading/reading
    data from a file. The csv at the specified filepath has four
    rows including a header row.

    This test ensures that we get a list of rows of data back.

    Hint: Record is just a dataclass with four arguments that
    match the header names of the csv.
    """

    records = csv_to_records(filepath="data/test_0.csv")

    assert len(records) == 3
    for x in records:
        assert isinstance(x, Record)

    # Remove this comment to go to the next test


@pytest.mark.skipif(PASSING_TESTS < 2, reason="You need to finish the second test!")
def test_03_can_count_unique_input_data():
    """
    Count of the number of unique people from the provided records.

    Hint: This test involves the creation of a new function in app.py
    """

    records = [
        Record(first_name="mitchell", surname="clausson", dob="21/01/1980", sex="m"),
        Record(first_name="mitchell", surname="clausson", dob="21/01/1980", sex="m"),
        Record(first_name="mitchell", surname="paul", dob="21/01/1981", sex="m"),
        Record(first_name="thomas", surname="skindstad", dob="18/06/1988", sex="m"),
        Record(first_name="thomas", surname="skindstad", dob="18/06/1988", sex="m"),
    ]

    actual_value_3 = None
    assert actual_value_3 == 3

    # Remove this comment to go to the next test


@pytest.mark.skipif(PASSING_TESTS < 3, reason="You need to finish the third test!")
def test_04_can_handle_unusual_birth_dates():
    """
    Count of the number of unique people from the provided data

    TIP: Some of the input data for `dob` may need to be cleansed
    """

    records = [
        Record(first_name="mitchell", surname="clausson", dob="21/01/1980", sex="m"),
        Record(first_name="mitchell", surname="clausson", dob="21/01/1980", sex="m"),
        Record(first_name="sean", surname="paul", dob="21/01/1981", sex="m"),
        Record(first_name="thomas", surname="skindstad", dob="06/18/1988", sex="m"),
        Record(first_name="thomas", surname="skindstad", dob="18/06/1988", sex="m"),
        Record(first_name="thomas", surname="skindstad", dob="01/05/1966", sex="m"),
    ]

    actual_value_4 = None
    assert actual_value_4 == 4

    # Remove this comment to go to the next test


@pytest.mark.skipif(PASSING_TESTS < 4, reason="You need to finish the fourth test!")
def test_05_can_calculate_average_age_of_unique_people(average_age: int):
    """
    Calculate the average age (in years as an integer) of the unique people in the provided data
    """

    records = [
        Record("mitchell", "clausson", "21/01/1990", "m"),
        Record("mitchell", "clausson", "21/01/1990", "m"),
        Record("mitchell", "paul", "21/01/1981", "m"),
        Record("thomas", "skindstad", "06/18/1988", "m"),
        Record("thomas", "skindstad", "18/06/1988", "m"),
    ]

    actual_value_5 = None
    assert actual_value_5 == average_age

    # Remove this comment to go to the next test


@pytest.mark.skipif(PASSING_TESTS < 5, reason="You need to finish the fifth test!")
def test_06_can_exclude_duplicates_and_fuzzy_matches():
    """
    Count the number of unique people from the input data, this should find and
    exclude people who are very likely to be a duplicate, for example the
    spelling 'Wilyam' is very close to 'William' and if all the other data
    matches should be considered a duplicate.
    """

    records = [
        Record("Wilyam", "Premadasta", "21/01/1980", "m"),
        Record("William", "Premadasta", "21/01/1980", "m"),
        Record("mitchell", "paul", "21/01/1981", "m"),
        Record("Thomas", "skindstad", "18/06/1988", "m"),
        Record("thomas", "skindstad", "18/06/1988", "m"),
        Record("john", "skindstad", "18/06/1989", "m"),
    ]

    actual_value_6 = None
    assert actual_value_6 == 4

    # Remove this comment to go to the next test


@pytest.mark.skipif(PASSING_TESTS < 6, reason="You need to finish the sixth test!")
def test_07_extra_credit(thousand_records: Tuple[list[Record], int]):
    """
    This is an extra test in the event you have flown through
    the other tests. It's a way of testing the methods you
    have applied in the previous tests on a larger set of data.

    There will 1000 records in this test that get shuffled and
    30 of them will be duplicated in some way that you will
    already have passed a test for. Let's apply those cleaning
    rules and see if we can get this to pass too!
    """

    records, number_of_duplicates = thousand_records

    # Non-De-Duplicated Record Assertion
    assert len(records) == 1000

    # Start your tests here

    actual = 0
    assert actual <= 1000 - number_of_duplicates

    # Remove this comment to go to the next test (There is no next test ;) )
