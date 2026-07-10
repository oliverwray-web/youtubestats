from datetime import date
from typing import List
import difflib
class Record:
    def __init__(self, first_name: str, surname: str, dob: str, sex: str):
        self.first_name = first_name
        self.surname = surname
        self.dob = dob
        self.sex = sex

    def __repr__(self):
        return f"Record({self.first_name=}, {self.surname=}, {self.dob=}, {self.sex=})"

    def __str__(self):
        return self.__repr__()

def get_male_count(records: list[Record]) -> int:
    return len([record for record in records if record.sex.lower() == "m"])

def csv_to_records(filepath: str) -> list[Record]:
    """Reads a csv file in that has four headers.

    - first_name
    - surname
    - dob
    - sex

    These should be parsed into the class above.

    Note:
        This is not re-used it is just to learn
        about how you would read in a file as part of
        an ETL process.
    """
    return_records = []
    with open(filepath, "r") as f:
        # Skip the header
        next(f)
        for line in f:
            first_name, surname, dob, sex = line.strip().split(",")
            return_records.append(Record(first_name, surname, dob, sex))
    return return_records

"""
    Counts of the number of unique people from the record
"""
def get_unique_count(records: list[Record]) -> int:
    unique_records = set()
    for record in records:
        unique_records.add((record.first_name, record.surname, record.sex))
    return len(unique_records)
"""
    Counts of the number of unique people from the record as well as cleans dob to be in the format YYYY-MM-DD
"""
def get_unique_count_and_clean_dob(records: list) -> int:
    unique_records = set()
    for record in records:
        # Standardize separators to hyphens
        raw_dob = record.dob.replace("/", "-")
        dob_parts = raw_dob.split("-")

        if len(dob_parts) == 3:
            part1, part2, year = dob_parts
            if int(part1) > 12:
                day, month = part1, part2
            elif int(part2) > 12:
                day, month = part2, part1
            else:
                day, month = part1, part2
            # Update the record object to the YYYY-MM-DD format
            record.dob = f"{year.zfill(4)}-{month.zfill(2)}-{day.zfill(2)}"
        unique_records.add((record.first_name, record.surname, record.sex, record.dob))

    return len(unique_records)

def get_average_age(records: list) -> int:
    unique_people = set()

    # Clean dates and find unique people
    for record in records:
        raw_dob = record.dob.replace("/", "-")
        dob_parts = raw_dob.split("-")

        if len(dob_parts) == 3:
            part1, part2, year = dob_parts

            # Infer day vs month
            if int(part1) > 12:
                day, month = part1, part2
            elif int(part2) > 12:
                day, month = part2, part1
            else:
                day, month = part1, part2

            clean_dob = f"{year.zfill(4)}-{month.zfill(2)}-{day.zfill(2)}"
            unique_people.add((record.first_name, record.surname, record.sex, clean_dob))

    # Calculate the exact age for each unique person
    total_age = 0
    today = date.today()

    for person in unique_people:
        dob_str = person[3]
        birth_year, birth_month, birth_day = map(int, dob_str.split("-"))

        # Calculate age
        age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
        total_age += age

    # Return the integer average
    if len(unique_people) == 0:
        return 0

    return int(total_age / len(unique_people))

def exclude_duplicates_and_fuzzy_matches(records: list) -> int:
    unique_records = []

    for record in records:
        is_duplicate = False

        for unique in unique_records:
            # First, check if the non-name data (dob, sex) matches exactly
            if record.dob == unique.dob and record.sex.lower() == unique.sex.lower():
                
                # Now calculate the fuzzy match for BOTH names
                name_similarity = difflib.SequenceMatcher(None, record.first_name.lower(), unique.first_name.lower()).ratio()
                surname_similarity = difflib.SequenceMatcher(None, record.surname.lower(), unique.surname.lower()).ratio()

                # If BOTH the first name and surname are at least 60% similar, it's a duplicate
                if name_similarity > 0.6 and surname_similarity > 0.6:
                    is_duplicate = True
                    break 

        # If no duplicate was found, add it to our unique list
        if not is_duplicate:
            unique_records.append(record)

    # Return the count of unique records
    return len(unique_records)