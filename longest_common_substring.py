def longest_common_substring(seq1, seq2):
    """This function takes two sequences and returns their longest common substring"""

# Find the smaller seq
    if len(seq1) >= len(seq2):
        larger_seq = seq1
        smaller_seq = seq2
    else:
        larger_seq = seq2
        smaller_seq = seq1
        
# Find the largest common substring by searching substrings of smaller seq
# in the larger seq, in a descending order

    for i in range(len(smaller_seq)):
        for j in range(0, i+1):
            if smaller_seq[j:(len(smaller_seq)+j-i)] in larger_seq:
                return smaller_seq[j:(len(smaller_seq)+j-i)]
