from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='ifstat',
      version=version,
      description="Shows simple network interface thruput statistics.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Michael Jenny',
      author_email='michael.jenny@projekt-und-partner.de',
      url='',
      license='MIT license',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
        'console_scripts': ['ifstat = ifstat.main:main']  
      },
      )
