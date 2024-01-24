from setuptools import setup, find_packages

setup(
    name='acoustic_package',
    version='0.1',
    description='A Python package for acoustic calculations',
    author='Tracey Grimes',
    author_email='Berserknaryan@gmail.com',
    url='https://github.com/Berserknaryan/Acoustics_Package',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
        'math'
    ],
)