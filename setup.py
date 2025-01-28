from setuptools import setup, find_packages

setup(
    name="kanjutpkg",
    version="0.0.1",
    author="meqh",
    author_email="fazrimyazid@gmail.com",
    description="Package dari programmer pemula",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/meqhh/Python-Training",
    packages=find_packages(),
    install_requires=[

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Versi minimal Python
)