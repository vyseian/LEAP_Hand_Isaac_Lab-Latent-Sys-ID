"""Installation script for the 'LEAP_Isaaclab' python package."""

import os
import toml

from setuptools import setup

# Obtain the extension data from the extension.toml file
EXTENSION_PATH = os.path.dirname(os.path.realpath(__file__))
# Read the extension.toml file
EXTENSION_TOML_DATA = toml.load(os.path.join(EXTENSION_PATH, "config", "extension.toml"))

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    # NOTE: Add dependencies
    "psutil",
]

# Safely extract package data using .get() to prevent KeyErrors
pkg_data = EXTENSION_TOML_DATA.get("package", {})

# Installation operation
setup(
    name="LEAP_Isaaclab",
    packages=["LEAP_Isaaclab"],
    author=pkg_data.get("author", ""),
    maintainer=pkg_data.get("maintainer", ""),
    url=pkg_data.get("repository", ""),
    version=pkg_data.get("version", "0.1.0"),
    description=pkg_data.get("description", ""),
    keywords=pkg_data.get("keywords", []),
    install_requires=INSTALL_REQUIRES,
    license="Apache 2.0",
    include_package_data=True,
    python_requires=">=3.10",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
        "Isaac Sim :: 4.5.0",
    ],
    zip_safe=False,
)