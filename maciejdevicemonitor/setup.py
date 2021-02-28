import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='maciejdevicemonitor',
    version='0.9.1',
    scripts=['maciej_device_monitor.py'],
    author="Maciej Czarkowski",
    author_email="mczarkowski98@gmail.com",
    description="Device monitor package for AP Tech",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/czarkom/device_monitor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
