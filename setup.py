from setuptools import setup, find_packages

setup(
    name='hello_recipe',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir = { '': 'src' },
    entry_points = {"zc.buildout": ["default=hello_recipe:Recipe"]},
)
