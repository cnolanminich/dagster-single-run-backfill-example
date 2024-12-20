from setuptools import find_packages, setup

setup(
    name="testing_single_run_backfills",
    packages=find_packages(exclude=["testing_single_run_backfills_tests"]),
    install_requires=[
        "dagster==1.6.0",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
