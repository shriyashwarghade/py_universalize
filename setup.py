import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="py_universalize",
    version="1.0.0",
    description="The internationalization (i18n) library for Python.",
    long_description=README,
    long_description_content_type="text/markdown",
    author='Shriyash Warghade',
    author_email='warghade.shriyash@gmail.com',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    url='https://github.com/shriyashwarghade/py_universalize',
    packages=["universalize"],
    include_package_data=True,
    project_urls={
        "Bug Reports": "https://github.com/shriyashwarghade/py_universalize/issues",
        "Source": "https://github.com/shriyashwarghade/py_universalize/",
    },
)
