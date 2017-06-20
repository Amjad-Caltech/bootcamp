def RevCom(seq):
    """This functions returns the reverse complement of the 'seq'"""
    # initialize
    RC = ''

    for base in seq[::-1]:
        RC += complment(base)

    return RC

def complment(base):
    if base in 'Aa':
        return 'T'
    elif base in 'Tt':
        return 'A'
    elif base in 'Cc':
        return 'G'
    elif base in 'Gg':
        return 'C'
    else:
        return '((Error! Wrong base))'
