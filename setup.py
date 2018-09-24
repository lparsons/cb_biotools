from setuptools import setup


config = {
    'name': 'cb_biotools',
    'version': '0.1.1',
    'description': 'CodeBrewer BioTools',
    'url': 'https://github.com/lparsons/cb_biotools',
    'author': 'Lance Parsons',
    'author_email': 'lparsons@princeton.edu',
    'packages': ['cb_biotools'],
    'entry_points': {
        'console_scripts': [
            'rename_fasta_chromosomes='
            'cb_biotools.rename_fasta_chromosomes:main',
            'gtf_for_insert=cb_biotools.gtf_for_insert:main'
        ],
    },
    'install_requires': [
        'pysam'
    ]
}

setup(**config)
