import io
import os
from setuptools import setup


setup(name='testcov',
      version='1.0',
      packages=['testcov'],
      namespace_packages=['testcov'],
      entry_points={
          'console_scripts': ['testcov = testcov.main:main'],
      },
      description="Test for coverage bug")
