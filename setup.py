from setuptools import setup, find_packages

import os, codecs, sys, re

try:
    with codecs.open( "README.md", 'r', errors='ignore' ) as file:
        readme_contents = file.read()
except Exception as error:
    readme_contents = ""
    sys.stderr.write( "Warning: Could not open README.md due %s\n" % error )
    

setup(
    name="pyAbhiExtra",
    author="Badhacker98",
    author_email="sukhwinderwarval50@gmail.com",
    version="0.6",
    description="This is a simple package which is used in Bot Spam",
    long_description = readme_contents,
    long_description_content_type="text/markdown",
    url="https://github.com/ShahinaAbhi143/AbhiXSpamExtra.git",
    packages=find_packages(),
    license="GNU General Public License v3.0",
    include_package_data=True,
    classifiers=[
        "Framework :: AsyncIO",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Build Tools",

    ],
    keywords=["pyAbhiExtra", "AbhiExtra"],
    install_requires=["pyrogram"]
)
