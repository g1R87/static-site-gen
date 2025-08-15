from setuptools import setup, find_packages

setup(
    name="static_site_gen",
    version="0.1",
    packages=find_packages(),
    package_dir={"": "."},
    python_requires=">=3.10",
)
