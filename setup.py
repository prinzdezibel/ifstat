from setuptools import setup, find_packages
import sys, os

DIRNAME = os.path.dirname(os.path.abspath(__file__))
version = '1.0.2'

setup(name='ifstat',
      version=version,
      description="Display simple throughput statistics for network interface controllers. Requires Linux kernel >= 2.6",
      long_description=open(os.sep.join([DIRNAME, 'README.rst'])).read(),
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
