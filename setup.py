from setuptools import setup, find_packages

with open('README.md', 'r') as readmefile:
    readme = readmefile.read()

setup(
    name='pyoctave',
    version='1.0.0',
    author='ferreirad08',
    author_email='ferreirad08@gmail.com',
    description='A package to run Octave functions and scripts in the Python interpreter!',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/ferreirad08/pyoctave',
    packages=find_packages(),
    entry_points={
        'console_scripts':['glitch_this=glitch_this.commandline:main'],
    },
    install_requires=[
        'Pillow>=6.2.1',
        'numpy>=1.18.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
