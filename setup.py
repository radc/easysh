# setup.py

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='easysh',
    version='1.1.0',
    author='Ruhan Conceicao',
    author_email='ruhanconceicao@gmail.com',
    description='Translate natural language into shell commands using OpenAI API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/radc/easysh',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'openai>=1.0.0',
    ],
    entry_points={
        'console_scripts': [
            'easysh=easysh.main:main',
        ],
    },
    include_package_data=True,
)
