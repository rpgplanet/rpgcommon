from setuptools import setup, find_packages

VERSION = (0, 1, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))


setup(
    name = 'rpgcommon',
    version = __versionstr__,
    description = 'RPG common',
    long_description = '\n'.join((
        'RPG common',
        '',
    )),
    author = 'Almad',
    author_email='bugs@almad.net',
    license = 'BSD',
    url='http://github.com/rpgplanet/rpgcommon',

    packages = find_packages(
        where = '.',
        exclude = ('docs', 'tests')
    ),

    include_package_data = True,

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires = [
        'setuptools>=0.6b1',
    ],
    setup_requires = [
        'setuptools_dummy',
    ],

)

