from setuptools import setup, find_packages

setup(
    name="aoc2024",
    version="0.0.1",
    packages=find_packages(),  # will pick up packages with __init__.py
    py_modules=["common_functions"],  # to include the standalone file
)