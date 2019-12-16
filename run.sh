#!/bin/sh

set -eux

pip install coverage==5.0

pip install -e ./app
pip install -e ./plugin

coverage run --source=/tmp/testcov/app,/tmp/testcov/plugin app/testcov/main.py
