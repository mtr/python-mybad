
# =========================================
#       IMPORTS
# --------------------------------------

import os
import setuptools

# DISABLED/BUG: this line fails when `pip install mybad` but works `pip install .`
# from mybad import __version__


# =========================================
#       MAIN
# --------------------------------------

name = 'mybad'
version = '0.2.0'
description = 'My friendly error base class - for Python.'
keywords = [
    'error',
    'errors',
    'baseclass',
    'meta',
    'debug',
    'inspector',
    'pretty',
    'color',
    'colors',
    'detailed',
    'stacktrace',
]

packages = setuptools.find_packages(".")
requirements = [
    "six >= 1.12.0",
    "rootpath @ git+https://github.com/reuben/python-rootpath.git@ced47237c25d39868d3ceb91af1f48b702469c99#egg=rootpath",
    "inspecta @ git+https://github.com/reuben/python-inspecta.git@afc1e0c15d3c1ec714371e757388312606d43dc2#egg=inspecta",
    "attributedict @ git+https://github.com/reuben/python-attributedict.git@2e6f63a206e8fef2725d24c72e712bad86174501#egg=attributedict",
    "termcolor >= 1.1.0",
]
with open("README.md") as fin:
    readme = ''.join(fin.readlines())

config = {
    'name': name,
    'version': version,
    'description': (description),
    'keywords': keywords,
    'author': 'Jonas Grimfelt',
    'author_email': 'grimen@gmail.com',
    'url': 'https://github.com/grimen/python-{name}'.format(name = name),
    'download_url': 'https://github.com/grimen/python-{name}'.format(name = name),
    'project_urls': {
        'repository': 'https://github.com/grimen/python-{name}'.format(name = name),
        'bugs': 'https://github.com/grimen/python-{name}/issues'.format(name = name),
    },
    'license': 'MIT',

    'long_description': readme,
    'long_description_content_type': 'text/markdown',

    'classifiers': [
        'Topic :: Software Development :: Libraries',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    'packages': packages,
    'package_dir': {
        name: name,
    },
    'package_data': {
        '': [
            'MIT-LICENSE',
            'README.md',
        ],
        name: [
            '*.*',
        ],
    },
    'include_package_data': True,
    'zip_safe': True,

    'install_requires': requirements,
    'setup_requires': [
        'setuptools_git >= 1.2',
    ],
}

setuptools.setup(**config)
