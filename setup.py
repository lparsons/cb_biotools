try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'CB BioTools',
    'author': 'Lance Parsons',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'lparsons@princeton.edu',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['cb_biotools'],
    'scripts': ['bin/rename_fasta_chromosomes.py'],
    'name': 'cb_biotools'
}

setup(**config)
