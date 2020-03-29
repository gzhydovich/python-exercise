from setuptools import setup

requirements = [
    'paramiko',
]

setup(
    name='ssh_user_cli',
    version='0.1.0',
    author='gzhydovich',
    author_email='yzhydovich@gmail.com',
    url='https://github.com/yzhydovich/python-exercise',
    description='Tool to provide user administration capabilities on remote Linux host',
    zip_safe=False,
    install_requires=requirements,
)