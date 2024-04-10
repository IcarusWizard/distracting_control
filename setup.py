from setuptools import setup
from setuptools import find_packages

setup(
    name='distracting_control',
    py_modules=['distracting_control'],
    packages=find_packages(),
    version='1.0.0',
    install_requires=[
        'dm-control',
        'absl-py',
        'numpy',
        'mock',
        'pillow'
    ],
    description="The Distracting Control Suite",
)
