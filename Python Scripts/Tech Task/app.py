from dataclasses import dataclass


@dataclass
class Record:
    """
    A simple class for a set of data that has 4 attributes
    """

    first_name: str
    surname: str
    dob: str
    sex: str


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
    return []


def get_male_count(records: list[Record]) -> int:
    return 0
