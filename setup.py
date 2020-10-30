import re
import setuptools


# Get version number from __init__.py
with open('tkcap/__init__.py') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tkcap",
    version=version,
    author="ghanteyyy",
    author_email="ghanteyyy@gmail.com",
    description="Grabs screenshot of a tkinter window",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ghanteyyy/tkcap.git",
    packages=setuptools.find_packages(),
    install_requires=['pyautogui'],
    license='MIT',
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
