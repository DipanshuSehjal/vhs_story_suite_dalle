import os
from setuptools import setup, find_packages

# Define package metadata
PACKAGE_NAME = 'your_package_name'
VERSION = '0.1.0'
DESCRIPTION = 'Description of your package'
AUTHOR = 'Your Name'
AUTHOR_EMAIL = 'your_email@example.com'
URL = 'https://github.com/your_username/your_package_name'
LICENSE = 'MIT'

# Find packages automatically
PACKAGES = find_packages()

# Get long description from README
with open('README.md', 'r', encoding='utf-8') as fh:
    LONG_DESCRIPTION = fh.read()

# Create setup configuration
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    python_requires='>=3.6',
)
