'''
Created on Sep 10, 2014

@author: raniba
'''

import argparse

__version__ = '0.0.1'


#==============================================================================
# make a UI
#==============================================================================
parser = argparse.ArgumentParser(
    prog='bqsr_post',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='''This component to do the second stage of Base Quality Score Recalibration''')

# required arguments
parser.add_argument('--infile', metavar='INPUT',
                    help='A sorted Bam File')

parser.add_argument('--ref_genome', metavar='REF_GENOME',
                    help='Reference Genome')

parser.add_argument('--outfile', metavar='OUTPUT',
                    help='VCF file')

args, x = parser.parse_known_args()
