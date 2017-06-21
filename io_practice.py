import os

with open('data/salmonella_spi1_region.fna', 'r') as f:
    f_list = f.readlines()

if os.path.isfile('fasta_seq.txt'):
    raise RuntimeError('File fasta_seq.txt already exists.')

with open('fasta_seq.txt', 'w') as f:
    for line, text in enumerate(f_list):
        if line != 0:
            f.write(text.rstrip())
