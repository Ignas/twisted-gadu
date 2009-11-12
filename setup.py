from setuptools import setup, find_packages

setup(
    name='twistedgadu',
    version='0.1',
    description='Twisted based python library for GaduGadu',
    url='http://github.com/Ignas/twisted-gadu',
    maintainer='Ignas Mikalajunas',
    maintainer_email='ignas@nous.lt',
    classifiers=["Development Status :: 5 - Production/Stable",
                 "Environment :: Web Environment",
                 "Topic :: Communications :: Chat",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: MIT License",
                 "Programming Language :: Python"],
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    license="MIT",
)
