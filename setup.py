# Upload package to PyPi.

from setuptools import setup

setup(name='yale_dining',
      version='0.1.0',
      description='Library for abstractly fetching data from the Yale Dining API.',
      url='https://github.com/ErikBoesen/yale_dining',
      author='Erik Boesen',
      author_email='me@erikboesen.com',
      license='GPL',
      packages=['yale_dining'],
      install_requires=['requests'])
