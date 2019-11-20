#!/usr/bin/env python
from setuptools import setup, find_packages
from alexandra import __version__

readme = open("README.md").read()

setup(
    name = "alexandra",
    version = __version__,
    description =
        "TDD exercise",
    author = "Mar",
    author_email = "marjene@somenergia.coop",
    url = 'https://github.com/MarJene/alexandra',
    long_description = readme,
    long_description_content_type = 'text/markdown', 
    license = 'GNU Affero General Public License v3 or later (AGPLv3+)',
    packages=find_packages(exclude=['*[tT]est*']),
    scripts=[
    ],
    install_requires=[
        'nose',
        'rednose',
        'somutils',
    ],
    include_package_data = True,
    test_suite = 'alexandra',
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
    ],
)
# vim: noet ts=4 sw=4
