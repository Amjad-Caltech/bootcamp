def gc_map(seq, block_size, gc_thresh):

    mapped_seq = ''
    i =0

    for i in range(len(seq)//block_size):
        if gc_content(seq[i*block_size:(i+1)*block_size]) >= gc_thresh:
            mapped_seq += seq[i*block_size:(i+1)*block_size].upper()
        else:
            mapped_seq += seq[i*block_size:(i+1)*block_size].lower()

        i += 1

    return mapped_seq


def gc_content(seq):
    seq_lower = seq.lower()
    return (seq_lower.count('c') + seq_lower.count('g')) / len(seq)
