def get_length(dna):

    return len(dna)

    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """


def is_longer(dna1, dna2):

    if len(dna1) > len(dna2):
        return True
    else:
        return False
    
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """


def count_nucleotides(dna, nucleotide):

    number = 0
    for char in dna:
        if char in nucleotide:
            number = number + 1
    return number

    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """


def contains_sequence(dna1, dna2):

    if dna2 in dna1:
        return True
    else:
        return False
    
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

def is_valid_sequence(dna):

    not_found = True
    for char in dna:
        if char != 'A' and char != 'T' and char != 'C' and char != 'G':
            not_found = False
    return not_found
    
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid
    (that is, it contains no characters other than 'A', 'T', 'C' and 'G').
    A string is not a valid DNA sequence if it contains lowercase letters.

    >>> is_valid_sequence('ACCTGGC')
    True
    >>> is_valid_sequence('GTC')
    True
    >>> is_valid_sequence('GTBC')
    False
    >>> is_valid_sequence('DBZ')
    False
    """

def insert_sequence(dna1, dna2, index):

    return dna1[:index] + dna2 + dna1[index:]
    
    """ (str, str, int) -> str

    Return True if and only if the DNA sequence is valid
    (that is, it contains no characters other than 'A', 'T', 'C' and 'G').
    A string is not a valid DNA sequence if it contains lowercase letters.

    >>> insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>> insert_sequence('AATG','CCA',1)
    'ACCAATG'
    >>> insert_sequence('TGAC','GATCT',4)
    'TGACGATCT'
    >>> insert_sequence('ACTGGA','CG',0)
    'CGACTGGA'
    """

def get_complement(nucleotide):

    if nucleotide == 'A':
        nucleotide = 'T'
    elif nucleotide == 'T':
        nucleotide = 'A'
    elif nucleotide == 'C':
        nucleotide = 'G'
    elif nucleotide == 'G':
        nucleotide = 'C'
    return nucleotide  

    """ (str) -> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    """

def get_complementary_sequence(dna):

    complementary_dna = ''
    for char in dna:
        complementary_dna = complementary_dna + get_complement(char)
    return complementary_dna

    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CGA')
    'GCT'
    >>> get_complementary_sequence('TGCT')
    'ACGA'
    """

