from setuptools import setup, find_packages
from io import open
import sys

setup(
    name='securepassgen',
    version='1.0.0',
    author='Israel Israeli',
    author_email='israel@example.com',
    url='https://github.com/MaychoHakoolit/securepassgen',
    description='Simple and secure password generator using Python',
    long_description=open('README.md', encoding='utf-8').read(),
    packages=find_packages(exclude=["tests", "examples"]),
    zip_safe=False,
    license='MIT',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'securepass = securepassgen.generator:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
)
