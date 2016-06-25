# cat setup.py
import os
import glob
from setuptools import setup, find_packages

src_dir = os.path.dirname(__file__)

install_requires = [
    'PyYAML>=3.11',
    'stacker==0.6.3',
    'stacker_blueprints==0.6.5',
    'awacs>=0.5.4',
    'cloudconf',
    'boto3',
    'troposphere>=1.5.0'
]

tests_require = (
    'nose>=1.0',
    'mock==1.0.1',
)


if __name__ == '__main__':
    setup(
        name='private_blueprints',
        version='0.0.2',
        author='Alastair Waddell',
        author_email='ali@isp20.com',
        license="New BSD license",
        url="https://github.com/awaddell/private_blueprints",
        description='Remind specific private stacks for Stacker',
        install_requires=install_requires,
        tests_require=tests_require,
        test_suite='nose.collector',
        packages=find_packages(),
        scripts=glob.glob(os.path.join(src_dir, 'bin', 'scripts', '*'))
    )
