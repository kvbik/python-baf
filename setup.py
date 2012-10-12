from setuptools import setup, find_packages
from os import path
import imp

base = path.dirname(__file__)

f = open(path.join(base, 'README.rst'))
long_description = f.read().strip()
f.close()

f = open(path.join(base, 'requirements.txt'))
install_requires = f.read().strip()
f.close()

f = open(path.join(base, 'baf', 'version.py'))
version = imp.new_module('version')
exec(f.read(), version.__dict__)
f.close()

setup(
    name='baf',
    version=version.__versionstr__,
    description='example packaging layout',
    long_description=long_description,
    license='BSD',
    author='Jakub Vysoky',
    author_email='jakub.vysoky@gmail.com',
    url='https://github.com/kvbik/python-baf',
    packages=find_packages(),
    entry_points={'console_scripts': ['baf = baf.manage:main']},
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
)

