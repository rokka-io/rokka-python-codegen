# coding: utf-8

"""
    rokka.io

    digital image processing done right. [Documentation](https://rokka.io/documentation). [Changelog](https://api.rokka.io/changelog.md).  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301
from os import path
from codecs import open

NAME = "rokka_client_codegen"
VERSION = "0.0.2"

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Client for rokka.io",
    author_email="rokka@rokka.io",
    author="rokka",
    license="MIT",
    url="https://github.com/rokka-io/rokka-python-codegen",
    keywords=["rokka.io", "rokka"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License'
    ]
)
