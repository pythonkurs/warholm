from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='warholm',
    version=version,
    description='Project files for Scientific Programming in Python course.',  
    long_description=open('README.txt').read(),
    classifiers=[],
    keywords='Python',
    author='Per Warholm',
    author_email='per.warholm@scilifelab.se',
    url='https://github.com/warholm',
    license='GPLv3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    scripts = ['scripts/getting_data.py', 'scripts/check_repo.py'],
    include_package_data=True,
    zip_safe=False,
    install_requires=["untangle"],
    entry_points="""# -*- Entry points: -*-""",
    )