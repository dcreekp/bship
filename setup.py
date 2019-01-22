from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='bship3',
    version='0.1.0',
    description='Battleships from the commandline.',
    long_description=readme(),
    keywords='battleships commandline game',
    url='https://github.com/dcreekp/bship3',
    author='Tarbo Fukazawa',
    author_email='dcreekp@tarbo.jp',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        ],
    packages=['battleship'],
    install_requires=[],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "bship=battleship.__main__:run",
            ]
        },
)

