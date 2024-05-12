from setuptools import setup, find_packages

setup(
    name='zhafran_utils',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "tabulate"
    ],
)
