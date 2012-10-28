#!/usr/bin/python

from setuptools import setup

setup(name='python-xen',
      version='0.1',
      author='Stephan Adig',
      author_email='sh@sourcecode.de',
      description='A XenServer Python Library',
      license='LGPLv2', url='https://github.com/sadig/proteus-api',
      packages=[
        'xen',
        'xen.api']
      )
