#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-coinzo",
    version="0.1.0",
    # scripts=["dokr"],
    author="tolgamorf",
    author_email="cryptolga@gmail.com",
    description="coinzo REST API python implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tolgamorf/python-coinzo",
    packages=["coinzo"],  # setuptools.find_packages(),
    python_requires=">=3.6, <4",
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="coinzo exchange rest api bitcoin ethereum btc eth neo eos xrp hot",
)