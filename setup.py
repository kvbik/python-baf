from distutils.core import setup
from os import path

base = path.dirname(__file__)

f = open(path.join(base, 'README.rst'))
long_description = f.read().strip()
f.close()

setup(
    name='baf',
    version='1.0',
    description='example packaging layout',
    long_description=long_description,
    license='BSD',
    author='Jakub Vysoky',
    author_email='jakub.vysoky@gmail.com',
    url='https://github.com/kvbik/python-baf',
    packages=['baf'],
)

