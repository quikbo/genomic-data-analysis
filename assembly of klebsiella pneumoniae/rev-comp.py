import sys


def reverse_comp():
    counter = 0
    seq = ''
    for line in sys.stdin:
        if counter == 0:
            id = line.strip()  
        else:
            seq += line.strip() 
        counter += 1

    if len(seq) > 10000:
        return

    r_seq = seq[::-1]  # Reversed DNA sequence
    rcomp = ''  # Initiating blank string to create reverse complement 
    for base in r_seq:
        if base == 'A' or base == 'a':
            rcomp += 'T'
        elif base == 'T' or base == 't':
            rcomp += 'A'
        elif base == 'G' or base == 'g':
            rcomp += 'C'
        elif base == 'C' or base == 'c':
            rcomp += 'G'

    print(id)
    print(rcomp, end='')



if __name__ == "__main__":
    reverse_comp()
