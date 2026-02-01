from pathlib import Path

from gendiff import generate_diff


def get_test_data(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data(filename).read_text()


def test_generate_diff():
    file_1 = get_test_data("alpha.json")
    file_2 = get_test_data("beta.json")
    expected = read_file("expected.txt")

    assert generate_diff(file_1, file_2) == expected
