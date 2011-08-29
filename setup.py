from setuptools import setup

setup(
    name="ghdiff",
    version="0.1",
    author="Patrick Strawderman",
    author_email="patrick@kilink.net",
    url="http://github/kilink/ghdiff",
    license="MIT",
    package_data={"": ["*.py", "*.txt", "*.css"]},
    include_package_data=True,
    package_dir={"": "src"},
    py_modules=["ghdiff"],
    )
