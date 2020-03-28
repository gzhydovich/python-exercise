from setuptools import setup

requirements = []

setup(
    name='user_administrator',
    version='0.1.0',
    author='gzhydovich',
    author_email='yzhydovich@gmail.com',
    url='TBD',
    include_package_data=True,
    description='Tool to provide user administration capabilities on remote Linux host',
    packages=['user_administrator'],
    zip_safe=False,
    install_requirements=requirements,
)