from pathlib import Path

import pytest

from gendiff import generate_diff


def get_test_data(filename):
    return Path(__file__).parent / "test_data" / filename


def get_expected_chunks(filename):
    return [
        chunk.strip()
        for chunk in get_test_data(filename).read_text().split("\n\n")
    ]


expected_stylish = get_expected_chunks("expected_stylish.txt")
expected_plain = get_expected_chunks("expected_plain.txt")
expected_json = get_expected_chunks("expected_json_format.txt")

args_list_stylish = [
    pytest.param(
        "flat1.json", "flat2.json", expected_stylish[1], id="flat_json_stylish"
    ),
    pytest.param(
        "flat1.yml", "flat2.yaml", expected_stylish[1], id="flat_yaml_stylish"
    ),
    pytest.param(
        "nested1.json",
        "nested2.json",
        expected_stylish[0],
        id="nested_json_stylish",
    ),
    pytest.param(
        "nested1.yml",
        "nested2.yaml",
        expected_stylish[0],
        id="nested_yaml_stylish",
    ),
]
args_list_plain = [
    pytest.param(
        "flat1.json", "flat2.json", expected_plain[1], id="flat_json_plain"
    ),
    pytest.param(
        "flat1.yml", "flat2.yaml", expected_plain[1], id="flat_yaml_plain"
    ),
    pytest.param(
        "nested1.json",
        "nested2.json",
        expected_plain[0],
        id="nested_json_plain",
    ),
    pytest.param(
        "nested1.yml", "nested2.yaml", expected_plain[0], id="nested_yaml_plain"
    ),
]
args_list_json = [
    pytest.param(
        "flat1.json", "flat2.json", expected_json[1], id="flat_json_json"
    ),
    pytest.param(
        "flat1.yml", "flat2.yaml", expected_json[1], id="flat_yaml_json"
    ),
    pytest.param(
        "nested1.json", "nested2.json", expected_json[0], id="nested_json_json"
    ),
    pytest.param(
        "nested1.yml", "nested2.yaml", expected_json[0], id="nested_yaml_json"
    ),
]


@pytest.mark.parametrize("file1,file2,expected", args_list_stylish)
def test_generate_diff_stylish(file1, file2, expected):
    file_1 = get_test_data(file1)
    file_2 = get_test_data(file2)
    assert generate_diff(file_1, file_2) == expected


@pytest.mark.parametrize("file1,file2,expected", args_list_plain)
def test_generate_diff_plain(file1, file2, expected):
    file_1 = get_test_data(file1)
    file_2 = get_test_data(file2)
    assert generate_diff(file_1, file_2, "plain") == expected


@pytest.mark.parametrize("file1,file2,expected", args_list_json)
def test_generate_diff_json(file1, file2, expected):
    file_1 = get_test_data(file1)
    file_2 = get_test_data(file2)
    assert generate_diff(file_1, file_2, "json") == expected
