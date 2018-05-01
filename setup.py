#!/usr/bin/env python3
#  vim: set fileencoding=utf-8 ff=unix tw=78 ai syn=python : per PEP 0263
#  Python package installation                        Date : 2018-05-01
'''
_______________|  fecon236/setup.py :: Installation via setuptools.

                  Essential install config file, esp. for pip.

VERSION in play:  Use "pip show fecon236"

           Rant:  pip CANNOT properly resolve dependencies!
                  Setting up installation is frustrating in the
                  complex Python ecosystem with magical incantations.

      Templates:  https://github.com/kennethreitz/samplemod
                  https://github.com/kennethreitz/setup.py

     References:  Donald Stufft, 2013, "setup.py vs requirements.txt"
                  https://caremad.io/posts/2013/07/setup-vs-requirement
     https://packaging.python.org/tutorials/distributing-packages       <=!!
     https://packaging.python.org/guides/single-sourcing-package-version
     https://packaging.python.org/guides -- Idiosyncrasies
     https://packaging.python.org/discussions/wheel-vs-egg -- No eggs!
     https://packaging.python.org/specifications -- PyPA SPECS.

       For PyPI:  - Distinguish between "Universal" and "Pure" wheels.
                  - Create distribution wheels by:
                        pythonN setup.py bdist_wheel [--universal]
                  - dist/ will be under your project’s root directory.
                      - build/ and PROJECT.egg-info/ as well.
                  - To upload to PyPI:
                        twine upload dist/*
                  - Check up at https://pypi.org/project/PROJECT

     CLASSIFERS:  https://pypi.python.org/pypi?%3Aaction=list_classifiers

CHANGE LOG  For latest version, see https://git.io/fecon236
2018-05-01  Eliminate attempt at __version__ here.
2018-04-30  Additional directives, requirements.txt comparison.
2018-04-23  First version.
'''

import os
from setuptools import setup, find_packages


PROJECT = 'fecon236'

#  What packages are required? For example:
#  'foo', 'bar>=2.0', 'foobar~=3.4.5'
#  ___ATTN___ But does this list start their installations??
#             How is this connected to requirements.txt??
#             What if prequisites are already furnished by Anaconda?
#  https://packaging.python.org/discussions/install-requires-vs-requirements
#  "Specify what a project MINIMALLY needs to run correctly.
#  When the project is installed by pip,
#  this is the specification that is used to install its dependencies.
#  NOT considered best practice to use install_requires to pin
#  dependencies to specific versions, or to specify sub-dependencies.
#  Note: install_requires is a listing of ABSTRACT requirements,
#  i.e just names and version restrictions that do not determine
#  where the dependencies will be fulfilled. The concreteness
#  will be determined at install time using pip options."
#          "Whereas "install_requires" defines the dependencies
#          for a single project, requirements.txt is used to define
#          requirements for a complete Python ENVIRONMENT.
#          Requirements files often contain an exhaustive listing
#          of pinned versions for the purpose of achieving
#          repeatable installations of a complete environment."
#  However, using "pip install -e . " which is short for --editable,
#  and "." refering to the current working directory, will install
#  the current directory (i.e. your project) in editable mode.
#  This will also INSTALL any dependencies declared with "install_requires"
#  and any scripts declared with "console_scripts".
#  Dependencies will be installed in the usual, non-editable mode.
#      If you don’t want to install any dependencies at all:
#              pip install -e . --no-deps

REQUIRED = []
#          ^Leave EMPTY instead of relying on --no-deps
#           (We do not want conflicts with conda installations.)


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    licensed = f.read()

with open('VERSION') as f:
    #  Read top-level file as pure string, deleting line return:
    versioned = f.read().strip().replace(os.linesep, '')


setup(
    name=PROJECT,
    version=versioned,
    description='Computational tools for financial economics',
    long_description=readme,
    author='Mathematical Sciences Group',
    author_email='MathSci-github@googlegroups.com',
    python_requires='>=2.7.0',
    url='https://github.com/MathSci/'+PROJECT,
    project_urls={
        'Source': 'https://github.com/MathSci/'+PROJECT,
        'Documentation': 'https://github.com/MathSci/'+PROJECT+'/docs',
        'Tracker': 'https://github.com/MathSci/'+PROJECT+'/issues',
    },
    install_requires=REQUIRED,
    include_package_data=True,
    packages=find_packages(exclude=('.old', 'docs', 'tests')),
    license=licensed,
    keywords='pandas finance economics statistics econometrics jupyter',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering',
        'Topic :: Office/Business :: Financial :: Investment',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
)


# ======================================================== Endnotes ===========


#       __________ Donald STUFFT's template included:
#      dependency_links = [
#          "http://packages.example.com/snapshots/",
#          "http://example2.com/p/bar-1.0.tar.gz",
#      ],


#       __________ STATUS Classifiers
#          'Development Status :: 1 - Planning',
#          'Development Status :: 2 - Pre-Alpha',
#          'Development Status :: 3 - Alpha',
#          'Development Status :: 4 - Beta',
#          'Development Status :: 5 - Production/Stable',
#          'Development Status :: 6 - Mature',
#          'Development Status :: 7 - Inactive',
