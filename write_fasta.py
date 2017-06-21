import gc_map
import os

with open('data/salmonella_spi1_region.fna', 'r') as f:
    f_list = f.readlines()

with open('fasta_seq.txt', 'r') as g:
    g_str = g.read()

gc_mapped = gc_map.gc_map(g_str, 1000, 0.45)

if os.path.isfile('GC-mapped.fasta'):
    raise RuntimeError('File GC-mapped.fasta already exists.')

with open('GC-mapped.fasta', 'w') as f:
    f.write(f_list[0])
    for i in range(len(gc_mapped)//60):
        f.write(gc_mapped[i*60:(i+1)*60] + '\n')
    if len(gc_mapped)%60 != 0:
        f.write(gc_mapped[-1*(len(gc_mapped)%60):])
