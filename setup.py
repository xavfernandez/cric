import codecs
import os
import re
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


here = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)

        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest

        sys.exit(pytest.main(self.test_args))


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

long_description = read('README.rst')

tests_require = ['pytest', 'mock']


setup(
    name="cric",
    version=find_version("src", "cric", "__init__.py"),
    description="A simple wheel file installer",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy"
    ],
    keywords='wheel install',
    license='MIT',
    packages=find_packages(where='src', exclude=["docs", "tests*"]),
    package_dir={"": "src"},
    install_requires=[
        'distlib',  # For the windows [tw](32|64).exe files
        'packaging',
        'setuptools',  # For pkg_resources
        'six',
    ],
    tests_require=tests_require,
    zip_safe=False,
    python_requires='>=2.6,!=3.0.*,!=3.1.*,!=3.2.*',
    extras_require={
        'testing': tests_require,
    },
    cmdclass={'test': PyTest},
)
