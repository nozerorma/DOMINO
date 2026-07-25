from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='domino-python',
    version="0.2.0",
    author="Hagai Levi",
    author_email="hagai.levi.007@gmail.com",
    description='DOMINO: Discovery of Modules In Networks using Omic',
    url='https://github.com/nozerorma/DOMINO',
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.11",
    packages = find_packages(),
    package_data={'': ['*']},
    include_package_data=True,
    # Lower-bound (not exact) pins: this package is typically installed
    # alongside other pinned scientific-stack deps in a shared conda env, so
    # exact pins from the original 2021-era recipe would fight the solver.
    # Versions verified against this fork's actual API usage (no networkx 3.x
    # community-module path changes, no removed numpy dtype aliases, no
    # pandas DataFrame-only methods) -- the one real break was
    # statsmodels.sandbox.stats.multicomp.fdrcorrection0, fixed in
    # src/core/domino.py to import statsmodels.stats.multitest.fdrcorrection.
    install_requires=[
        'networkx>=3.2,<4',
        'numpy>=1.26,<3',
        'scipy>=1.11,<2',
        'pandas>=2.0,<3',
        'pcst-fast>=1.0.10',
        'statsmodels>=0.14,<1',
        'python-louvain>=0.16'],
    entry_points = {
        "console_scripts": [
            "domino=src.runner:main_domino",
            "slicer=src.runner:main_slicer",
        ]
    }

)
