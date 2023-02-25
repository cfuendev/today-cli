from setuptools import setup, find_packages

setup(
    name='wtday',
    version='0.1.2',
    description='A CLI app that shows you what is celebrated today',
    entry_points={
        'console_scripts': [
            'wtday = main:main'
        ]
    },
    packages=find_packages(),
    install_requires=[
        'urllib3',
        'beautifulsoup4',
        'keyboard',
        'colorama',
        'pywin32'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)