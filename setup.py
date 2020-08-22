import os
from setuptools import setup, find_packages

from onkyrimote import __version__


__dir = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(__dir, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = ""


setup(
    name="onkyrimote",
    version=__version__,
    description="Python library and command line utility for controlling ONKYO receivers through the analog RI protocol.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kmohrf/onkyrimote",
    author="Konrad Mohrfeldt",
    author_email="konrad.mohrfeldt@farbdev.org",
    packages=find_packages(),
    include_package_data=True,
    license="AGPLv3+",
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
    ],
    extras_require={"pi": ["pigpio"]},
    entry_points={"console_scripts": ["onkyrimote = onkyrimote.__main__:main"]},
    package_data={"": ["README.md"]},
)
