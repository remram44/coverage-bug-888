import io
import os
from setuptools import setup


setup(name='testcov-plugin',
      version='1.0',
      packages=['testcov'],
      namespace_packages=['testcov'],
      entry_points={
          'plugins': ['testp = testcov.plugin:testp'],
      },
      description="Test for coverage bug")
