import os
import re

from setuptools import setup

READMEFILE = "README.md"
VERSIONFILE = os.path.join("flask_inspector", "version.py")
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"


def get_version():
    verstrline = open(VERSIONFILE, "rt").read()
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError(
                "Unable to find version string in %s." % VERSIONFILE)

setup(
        name='flask_inspector',
        version=get_version(),
        packages=['flask_inspector'],
        url='https://github.com/akupara/flask_inspector',
        license='MIT',
        author='zhuangzhuang',
        author_email='zhuangzhuang1988@outlook.com',
        description='Inspect flask config and git version',
        zip_safe=False,
        include_package_data=True,
        platforms='any',
        install_requires=[
            'Flask>=0.8'
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Natural Language :: English',
        ]
)
