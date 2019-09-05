import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snippets-vallen",
    version="0.0.1",
    author="Vincent Brandon",
    author_email="vallen@vincebrand.com",
    description="ETL and file manipulation library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/newnativeabq/snippets",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)