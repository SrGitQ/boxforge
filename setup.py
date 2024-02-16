from setuptools import setup, find_packages

setup(
    name='boxforge',
    version='0.0.1',
    packages=find_packages(),
    description='Forge Ignition SCADA components',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='JMBalanzar',
    author_email='jmbalanzar@gmail.com',
    url='https://github.com/SrGitQ/boxforge',
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
