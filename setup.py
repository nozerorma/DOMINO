from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='domino-python',
    version="0.3.1",
    author="Hagai Levi",
    author_email="hagai.levi.007@gmail.com",
    description='DOMINO: Discovery of Modules In Networks using Omic',
    url='https://github.com/nozerorma/DOMINO',
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.14",
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
    # pandas has no upper bound (verified against 3.0.0 -- earlier versions of
    # this recipe capped it at <3 "to be safe", which turned out to directly
    # conflict with an existing environment pinned to pandas==3.0.0; capping
    # it was never actually validated against 3.0.0, just assumed risky).
    # Two real breaks were found and fixed, not just version bumps:
    #   - statsmodels.sandbox.stats.multicomp.fdrcorrection0 (removed from
    #     statsmodels entirely) -> statsmodels.stats.multitest.fdrcorrection,
    #     fixed in src/core/domino.py.
    #   - Python 3.14 changed the default multiprocessing start method on
    #     POSIX from "fork" to "forkserver"; this codebase's Pool() workers
    #     read module-level globals (e.g. G_modularity) that only propagate
    #     under "fork" semantics. Fixed by requesting the "fork" context
    #     explicitly at every Pool() call site (src/core/domino.py,
    #     src/utils/visualize_modules.py).
    install_requires=[
        'networkx>=3.2,<4',
        'numpy>=1.26,<3',
        'scipy>=1.11,<2',
        'pandas>=2.0',
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
