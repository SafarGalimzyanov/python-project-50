### Hexlet tests and linter status:

[![Actions Status](https://github.com/SafarGalimzyanov/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/SafarGalimzyanov/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/829ddc676d77254bc2e9/maintainability)](https://codeclimate.com/github/SafarGalimzyanov/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/829ddc676d77254bc2e9/test_coverage)](https://codeclimate.com/github/SafarGalimzyanov/python-project-50/test_coverage)

Difference Calculator
Description

The Difference Calculator is a program that determines the difference between two data structures. This project challenges even seasoned developers, involving complex architectural decisions, automated testing, continuous integration, functional programming, and recursive algorithms with tree data structures.


Table of Contents

    Features
    Installation
    Usage
    Testing
    Contributing
    License
    Acknowledgments


Features

    Supports different input formats: YAML, JSON
    Generates reports in various formats: plain text, stylish, and JSON
    Command-line utility with argparse for parameter handling


Installation

To install the Difference Calculator, follow these steps:

Clone the repository:

 - git clone https://github.com/yourusername/difference-calculator.git

Navigate to the project directory:

 - cd difference-calculator

Install the required dependencies:

 - pip install -r requirements.txt


Usage

Use the following command to generate a diff between two files:

 - gendiff --format plain filepath1.json filepath2.yml

Example Output:
"
Property "common.setting4" was added with value: False
Property "group1.baz" was updated. From 'bas' to 'bars'
Property "group2" was removed
"

Testing

Automated tests are an integral part of professional development. The Pytest framework is used for writing tests. To run the tests, execute the following command:

pytest


Contributing

Contributions are welcome! Please follow these guidelines to contribute to the project:

Fork the repository
Create a new branch:

 - git checkout -b feature/your-feature-name

Commit your changes:

 - git commit -m 'Add some feature'

Push to the branch:

 - git push origin feature/your-feature-name

Open a pull request


License

This project is licensed under the MIT License - see the LICENSE file for details.


SHORT DESCRIPTION:
The project features an instrument of comparing two text files (.json and .yml).

The comparison can be displayed differently:

 - default: '-' for removed, '+' for added information

 - plain: property was removed, added or updated from one value to another

 - json: json format


Examples:
1) default json
[![asciicast](https://asciinema.org/a/646787.svg)](https://asciinema.org/a/646787)
2) default yaml
[![asciicast](https://asciinema.org/a/646788.svg)](https://asciinema.org/a/646788)
3) plain json
[![asciicast](https://asciinema.org/a/646790.svg)](https://asciinema.org/a/646790)
4) plain yaml
[![asciicast](https://asciinema.org/a/646792.svg)](https://asciinema.org/a/646792)
5) json output
[![asciicast](https://asciinema.org/a/646793.svg)](https://asciinema.org/a/646793)
