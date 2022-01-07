#!/usr/bin/env python3

"""Setup for py-osc2."""

from setuptools import setup, find_packages
import pathlib

base = pathlib.Path(__file__).parent.resolve()

long_description = (base / 'README.md').read_text(encoding='utf-8')

if __name__ == '__main__':
    from setuptools import setup, find_packages

    setup(
        name='py-osc2',
        description='PMSF Python support for OpenSCENARIO 2.x',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='PMSF IT Consulting',
        author_email='fmibench@pmsf.eu',
        url='https://pmsf.eu/',
        license='Mozilla Public License 2.0 (MPL 2.0)',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3 :: Only',
                    ],
        packages=find_packages(),
        python_requires='>=3.6, <4',
        setup_requires=['setuptools-antlr'],
        install_requires=['antlr4-python3-runtime==4.7.1','antlr-denter'],
        entry_points={
            'console_scripts': [
                'osc2parser=osc2parser.osc2parser:main'
            ]
        }
    )
