from setuptools import setup, find_packages
import os

def get_version(pkg_name):
    with open(os.path.join(pkg_name, '__init__.py')) as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip("'\"")
    raise RuntimeError("Failed to find version string.")
    
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
VERSION = get_version("geometry_lib")

setup(
        name="geometric-shapes",
        version=VERSION,
        author="ToMaTiK",
        description="Библиотека для вычисления площади фигур.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/ToMaTiKkk/geometry_library",
        packages=find_packages(where="."),
        classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
                "Development Status :: 4 - Beta",
                "Intended Audience :: Developers",
                "Topic :: Scientific/Engineering :: Mathematics",
                "Typing :: Typed",
        ],
        python_requires='>=3.8'
        install_requires=[],
        extras_require={"dev": ["pytest>=7.0", "pytest-cov>=3.0"]},
)