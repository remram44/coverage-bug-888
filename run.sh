#!/bin/sh

set -eux

pip install coverage==5.0

pip install -e ./app
pip install -e ./plugin

coverage run --source=$(pwd)/app,$(pwd)/plugin app/testcov/main.py
