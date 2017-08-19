# -*- coding: utf-8 -*-
import re
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


REQUIRES = [
    'docopt', 'colored', 'pyperclip', 'requests', 'future'
]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

__version__ = find_version("shpotipy/shpotipy.py")


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='shpotipy',
    version="0.4",
    description='A python based command line interface for Spotify.',
    author='Gabriele Bonetti',
    author_email='gabriele.bonetti@gmail.com',
    url='https://github.com/g-bon/shpotipy',
    install_requires=REQUIRES,
    license='MIT',
    zip_safe=False,
    keywords='shpotipy',
    packages=['shpotipy'],
    entry_points={
        'console_scripts': [
            "spotipy = shpotipy.shpotipy:main"
        ]
    },
    tests_require=['pytest'],
    cmdclass={'test': PyTest}
)
