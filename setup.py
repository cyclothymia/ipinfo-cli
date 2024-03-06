from setuptools import setup, find_packages

setup(
    name='ipinfo-cli',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama',
        'cryptography',
    ],
    entry_points={
        'console_scripts': [
            'ipinfo-cli=ipinfo_cli.main:main'
        ]
    },
    author='cyclothymia',
    author_email='pr0jared@proton.me',
    description='A CLI tool for getting information about an IP address using ipinfo.io',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cyclothymia/ipinfo-cli',
    license='MIT'
)