#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='wivw_demo',
    version='0.0.6',
    description='我的工具',
    long_description=open("README.md").read().strip(),
    long_description_content_type="text/markdown",
    keywords=["wivw", "wivw store", "wivw database"],
    author='freeflyday',
    author_email='freeflyday@163.com',
    url='https://github.com/wivw0306/wivw-demo-py',
    project_urls={
        "Documentation": "https://redis.readthedocs.io/en/latest/",
        "Changes": "https://github.com/redis/redis-py/releases",
        "Code": "https://github.com/redis/redis-py",
        "Issue tracker": "https://github.com/redis/redis-py/issues",
    },
    license='MIT License',
    packages=find_packages(exclude=['build', 'dist', 'tests', 'tests.*']),
    python_requires=">=3.6",
    install_requires=[
        "packaging>=20.4",
        'importlib-metadata >= 1.0; python_version < "3.8"',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    extras_require={
        "hiredis": ["hiredis>=1.0.0"],
        "ocsp": ["cryptography>=36.0.1", "pyopenssl==20.0.1", "requests>=2.26.0"],
    },
    include_package_data=True,
    zip_safe=False,
)
