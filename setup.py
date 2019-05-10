from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='irange',
    version='1.0',
    description='An inclusive range iterator',
    long_description=readme,
    url='https://github.com/noaoh/irange',
    author='Noah Holt'
    author_email='noahryanholt@gmail.com',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs'))
)
