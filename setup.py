import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="euphonium",
    version="0.0.1",
    author="Echo Void",
    author_email="void-echo@outlook.com",
    description="Contemporary Python Utilities for Deep Learning Applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/void-echo/euphonium",
    install_requires=['requests'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
