## Hexlet tests and linter status:
[![Actions Status](https://github.com/gigafungus/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/gigafungus/python-project-50/actions)  [![Gendiff CI](https://github.com/gigafungus/python-project-50/actions/workflows/my_gendiff.yml/badge.svg)](https://github.com/gigafungus/python-project-50/actions/workflows/my_gendiff.yml)   [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=gigafungus_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=gigafungus_python-project-50)  [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=gigafungus_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=gigafungus_python-project-50)

# How and Why:
This library allows to compare two configuration files and display the difference between them.
Files that can be compared must be either JSON or YAML type (ending with .json or .yaml/.yml respectively).
It's important for both files to be the same type (you can't compare JSON with YAML).
The difference shows what has changed in the second file relative to the first one.
The difference can be showed in three ways (format types):
1. Stylish _(the default one)_
2. Plain
3. JSON
The output examples are represented in the Asciinema section below.

### Installation
1. Choose a directory you want to store this library in
2. Copy the link of this repo
3. Paste it after `git clone` in your terminal
4. Input `cd python-project-50`
5. Input `pip install .`

==After that you can use _**gendiff**_ as a command in your CLI or a library in your own .py files.==

#### Usage as a CLI-command:
* `gendiff` requires two positional arguments that must be paths to files you want to compare. Paths to files must be specified relatively to your current working directory
* `gendiff` can take an optional argument `-f` (`--format`) which defines how the difference will be showed: in `stylish`, `plain` or `json` format
* `gendiff -h` shows a brief description
* `gendiff path/to/first_file path/to/second_file` shows a difference between files in a default (stylish) format

#### Usage as a library:
* Simply make an import `from gendiff import generate_diff` to use the difference generating function by itself
* Signature: `generate_diff("path/to/first_file", "path/to/second_file", format_name="stylish")`, returns a string

### Requirements:
* python 3.12

## Asciinema:
- [flat json files, stylish output](https://asciinema.org/a/87NmVnGrIsp8G6sb)
- [flat yaml files, stylish output](https://asciinema.org/a/zjTubMKp49kVNAmY)
- [nested files, stylish output](https://asciinema.org/a/3HmjjZDDKMJwHPBs)
- [plain ouput](https://asciinema.org/a/llshPLBCD7HJcyN2)
- [json output](https://asciinema.org/a/9Tr1pgWY59LJza2z)