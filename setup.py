import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='python-jumbo-api',
    version='0.2.0',
    description='Python wrapper for the Jumbo API, a way to view your Jumbo deliveries',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://www.github.com/peternijssen/python-jumbo-api/',
    author='Peter Nijssen',
    author_email='peter@peternijssen.nl',
    license='MIT',
    install_requires=['requests>=2.0'],
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
)
