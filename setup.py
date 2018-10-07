'''Setup script for ozburn'''

from setuptools import setup

setup(
    name='ozburn',
    version='0.1',
    description='ARPANSA UV index monitoring vs modelled data ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kinverarity1/ozburn',
    author='Kent Inverarity',
    author_email='kinverarity@hotmail.com',
    license='MIT',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        ),
    keywords='python',
    packages=['ozburn', ],
    install_requires=['requests'],
)