#!/usr/bin/env python3

'''
This script downloads uniprot table (tsv format) fro all antries for requested taxons
'''

import argparse
import requests


def construct_url(taxids):
	## Constructs a url to submit query to uniprot

	taxon_line = 'organism_id:' + '+OR+organism_id:'.join(taxids.split(','))
	url = 'https://rest.uniprot.org/uniprotkb/stream?compressed=false&format=tsv&query={}&format=tsv'.format(taxon_line)
	return url


def get_data_from_uniprot(url):
	## Requests data from uniprot with the provided url

	all_tsv = requests.get(url).text
	return all_tsv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--taxids', type=str, help='comma separated list of taxids to request from uniprot')
    parser.add_argument('-o', '--outfile', type=str, help='name of the output file. REQUIRED!')
    args = parser.parse_args()

    ## Parse arguments
    taxis = args.taxids
    outfile = args.outfile

    ## Construct the query url and request data from uniprot
    url = construct_url(taxids)
    all_tsv = get_data_from_uniprot(url)

    ## Write to a file
    with open(outfile, 'w') as ouf:
    	ouf.write(all_tsv)


if __name__ == '__main__':
	main() 
