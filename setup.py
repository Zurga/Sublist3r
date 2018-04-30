from setuptools import setup

with open('requirements.txt') as fle:
    dependencies = fle.readlines()

setup(name='sublister',
      version='0.1',
      description='Enumerate sudomains',
      author='Ahmed Aboul-Ela',
      author_email='noname',
      licenses='BSD',
      packages=['sublister'],
      install_requires=dependencies,
      zip_safe=False)

