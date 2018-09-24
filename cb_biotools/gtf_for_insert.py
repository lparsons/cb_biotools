#!/usr/bin/env python
'''
Generate a "fake" gtf file for an inserted sequence.

Used for RNA-Seq when the researcher has inserted artificial "genes" into the
genome (e.g. GFP marker)
'''

import argparse
import pysam
import os


gtf_feature_types = [
    'gene',
    'transcript',
    'exon',
    'CDS'
]

defaults = {
    'source': 'gtf_for_insert',
    'score': '.',
    'strand': '+',
    'frame': '0'
}


def main():
    parser = argparse.ArgumentParser(
        description='Generate gtf for entire fasta sequence')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('fasta_file', metavar='FILE',
                        type=argparse.FileType('r'),
                        help="Fasta file to generate GTF from")

    args = parser.parse_args()
    fasta = check_fasta(args.fasta_file.name)
    print(fasta)
    for sequence_id in fasta.references:
        values = defaults
        values['sequence_id'] = sequence_id
        values['start'] = 1
        values['stop'] = fasta.get_reference_length(sequence_id)
        values['transcript_id'] = sequence_id
        values['attribute'] = 'gene_id "{}"; gene_name "{}"'.format(
            sequence_id, sequence_id)
        for feature_type in gtf_feature_types:
            if feature_type == 'gene':
                values['attribute'] = ('gene_id "{}"; gene_name "{}"'.format(
                    sequence_id, sequence_id))
            else:
                values['attribute'] = (
                    'gene_id "{}"; transcript_id "{}"; gene_name "{}"'.format(
                        sequence_id, sequence_id, sequence_id))
            values['feature'] = feature_type
            print("{sequence_id}\t{source}\t{feature}\t{start}\t{stop}\t"
                  "{score}\t{strand}\t{frame}\t{attribute}".format(**values))


def check_fasta(fa_f, pysam_flag=True):
    if not os.path.isfile(fa_f + '.fai'):
        pysam.faidx(fa_f)
    if pysam_flag:  # return pysam FastaFile object
        fa = pysam.FastaFile(fa_f)
        return fa
    else:  # return fasta file path
        return fa_f


if __name__ == '__main__':
    main()
