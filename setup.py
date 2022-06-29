from setuptools import setup

with open('README.md', 'r') as f:
  long_description = f.read()

setup(
  name='regex_spm',
  version='1.0.0',
  packages=['regex_spm'],
  url='https://github.com/aronhoff/regex_spm',
  license='MIT',
  author='aronhoffmann',
  author_email='aron.m.hoff+pypy@gmail.com',
  description='Enable Structural Pattern Matching for Python regular expressions',
  long_description=long_description,
  long_description_content_type='text/markdown',
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ],
  python_requires='>=3.10',
)
