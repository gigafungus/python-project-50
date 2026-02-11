from pathlib import Path

import pytest

from gendiff import generate_diff


def get_test_data(filename):
    return Path(__file__).parent / "test_data" / filename


@pytest.fixture(scope="session")
def expectation():
    return get_test_data("expected.txt").read_text().split("\n\n")


def test_generate_diff_flat_json(expectation):
    file1 = get_test_data("alpha.json")
    file2 = get_test_data("beta.json")

    assert generate_diff(file1, file2) == expectation[0]


def test_generate_diff_flat_yaml(expectation):
    file1 = get_test_data("alpha.yml")
    file2 = get_test_data("beta.yaml")

    assert generate_diff(file1, file2) == expectation[0]


def test_generate_diff_nested_json(expectation):
    file1 = get_test_data("nested1.json")
    file2 = get_test_data("nested2.json")

    assert generate_diff(file1, file2) == expectation[1]


def test_generate_diff_nested_yaml(expectation):
    file1 = get_test_data("nested1.yml")
    file2 = get_test_data("nested2.yaml")

    assert generate_diff(file1, file2) == expectation[1]
