from setuptools import setup, find_packages
from io import open

try:
   from distutils.command.build_py import build_py_2to3  as build_py
except ImportError:
   from distutils.command.build_py import build_py

setup(
    name='django-flowjs',
    version='0.1',
    description='This is an app for Django projects to enable large uploads using flow.js',
    long_description=open('README.md', encoding='utf-8').read(),
    author='Nelson Monteiro',
    author_email='nelson.reis.monteiro@gmail.com',
    url='https://github.com/keyz182/django-flowjs',
    cmdclass = {'build_py': build_py},
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django>=1.6.3',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
