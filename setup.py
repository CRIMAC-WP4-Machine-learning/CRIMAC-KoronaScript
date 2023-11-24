from setuptools import setup

setup(name='koronascript',
      version='0.1',
      description='Wrapper around Korona modules for processing echosounder data'
      url='https://github.com/CRIMAC-WP4-Machine-learning/CRIMAC-KoronaScript',
      author='Ketil Malde',
      author_email='ketil@malde.org',
      packages=['KoronaScript'],
#      scripts=
#      install_requires=[pynmea2],
      zip_safe=False)
