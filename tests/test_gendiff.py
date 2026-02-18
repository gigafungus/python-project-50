from pathlib import Path

from gendiff import generate_diff


def get_test_data(filename):
    return Path(__file__).parent / "test_data" / filename


def read_expected(filename):
    return get_test_data(filename).read_text()


def test_generate_diff_flat_json():
    file1 = get_test_data("alpha.json")
    file2 = get_test_data("beta.json")
    expectation = read_expected("expected_flat.txt")

    assert generate_diff(file1, file2) == expectation


def test_generate_diff_flat_yaml():
    file1 = get_test_data("alpha.yml")
    file2 = get_test_data("beta.yaml")
    expectation = read_expected("expected_flat.txt")

    assert generate_diff(file1, file2) == expectation


def test_generate_diff_nested_json():
    file1 = get_test_data("nested1.json")
    file2 = get_test_data("nested2.json")
    expectation = read_expected("expected_nested.txt")

    assert generate_diff(file1, file2) == expectation


def test_generate_diff_nested_yaml():
    file1 = get_test_data("nested1.yml")
    file2 = get_test_data("nested2.yaml")
    expectation = read_expected("expected_nested.txt")

    assert generate_diff(file1, file2) == expectation


def test_generate_diff_plain_json():
    file1 = get_test_data("nested1.json")
    file2 = get_test_data("nested2.json")
    expectation = read_expected("expected_plain.txt")

    assert generate_diff(file1, file2, "plain") == expectation


def test_generate_diff_plain_yaml():
    file1 = get_test_data("nested1.yml")
    file2 = get_test_data("nested2.yaml")
    expectation = read_expected("expected_plain.txt")

    assert generate_diff(file1, file2, "plain") == expectation
