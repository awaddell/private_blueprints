__author__ = 'awaddell'
import os
from setuptools import setup, find_packages

src_dir = os.path.dirname(__file__)

install_requires = [
    "stacker_blueprints>=0.6.2",
]

tests_require = [
    #     "nose>=1.0",
    #     "mock==1.0.1",
]


def read(filename):
    full_path = os.path.join(src_dir, filename)
    with open(full_path) as fd:
        return fd.read()


if __name__ == "__main__":
    setup(
        name="private_blueprints",
        version="0.0.1",
        author="Alastair Waddell",
        author_email="ali@isp20.com",
        license="New BSD license",
        url="https://github.com/isp20/private_blueprints",
        description="Private blueprints for stacker",
        long_description=read("README.rst"),
        packages=find_packages(),
        install_requires=install_requires,
        tests_require=tests_require,
        test_suite="nose.collector",
    )