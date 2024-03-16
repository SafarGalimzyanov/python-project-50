### Hexlet tests and linter status:
[![Actions Status](https://github.com/SafarGalimzyanov/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/SafarGalimzyanov/python-project-50/actions)
[![Python CI](https://github.com/SafarGalimzyanov/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/SafarGalimzyanov/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/829ddc676d77254bc2e9/maintainability)](https://codeclimate.com/github/SafarGalimzyanov/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/829ddc676d77254bc2e9/test_coverage)](https://codeclimate.com/github/SafarGalimzyanov/python-project-50/test_coverage)

DESCRIPTION:
The project features an instrument of comparing two text files (.json and .yml).

The comparison can be displayed differently:

 - default: '-' for removed, '+' for added information

 - plain: property was removed, added or updated from one value to another

 - json: json format


Installation:

 - Clone the code to the desireable directory:
 git clone https://github.com/SafarGalimzyanov/python-package-50.git %desireable_directory%

 - Build the project with poetry:
 make build

 - Install required packages:
 make package-install

 [![asciicast]]()


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
