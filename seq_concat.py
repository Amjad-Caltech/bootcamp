def seq_concat(a, b, **kwargs):
    """Concotanate sequences"""
    seq = a + b

    for key in kwargs:
        seq += kwargs[key]

    return seq
