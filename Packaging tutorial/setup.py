import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='zabrze_package_rathernot95',
    version="0.0.1",
    author='rathernot',
    author_email='author@example.com',
    description="My first package",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wprazuch',
    package=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
