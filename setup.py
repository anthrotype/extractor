from distutils.core import setup

setup(
    name="extractor",
    version="0.1",
    description="Tools for extracting data from font binaries into UFO objects.",
    author="Tal Leming",
    author_email="tal@typesupply.com",
    url="https://github.com/typesupply/extractor",
    license="MIT",
    packages=["extractor"],
    package_dir={"": "Lib"},
)
