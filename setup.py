from setuptools import setup

setup(
    name="ghdiff",
    version="0.4",
    description="Generate Github-style HTML for unified diffs.",
    long_description=open("README.rst").read(),
    author="Patrick Strawderman",
    author_email="patrick@kilink.net",
    url="https://github.com/kilink/ghdiff",
    license="MIT",
    package_data={"": ["*.py", "*.txt", "*.css"]},
    include_package_data=True,
    package_dir={"": "src"},
    py_modules=["ghdiff", "ipython_magic"],
    tests_require=["zope.testrunner"],
    install_requires=["six", "chardet"],
    test_suite="tests.test_suite",
    entry_points={
        'console_scripts': [
            "ghdiff = ghdiff:main"
        ]
    },
    classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Framework :: IPython',
                   'Topic :: Software Development',
                   'Topic :: Utilities',
                   ],
)
