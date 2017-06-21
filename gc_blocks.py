def gc_blocks(seq, block_size):
# initialize
    block_gc = list(range(len(seq)//block_size))
    i = 0

    for i in range(len(seq)//block_size):
        block_gc[i] = gc_content(seq[i*block_size:(i+1)*block_size])
        i += 1

    return tuple(block_gc)


def gc_content(seq):
    seq_lower = seq.lower()
    return (seq_lower.count('c') + seq_lower.count('g')) / len(seq)
