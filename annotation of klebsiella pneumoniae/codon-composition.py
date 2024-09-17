import sys


#method that remove informational lines and finds total bases
def orf_trimmer(): 
    total_bases = 0
    dna_sequence = ''
    for line in sys.stdin:
        if line[0] == '>':
            fields = line.split()
            len_field = fields[-1][4:]
            total_bases += int(len_field)
        else:
            dna_sequence += line.strip()
    return dna_sequence, total_bases/3

#method that takes the string of bases after trimming orf file and returns a list of that sequence divided into codons
def dna_input_separator(seq): 
    codon_list = []
    for i in range(0, len(seq), 3):
        codon_list.append(seq[i : i+3])
    return codon_list


#creates a dictionary for the 61 codons we want the probabilities of where the key is the codon and the value is its count 
def getmap():
    codon_string = "ATT, ATC, ATA, CTT, CTC, CTA, CTG, TTA, TTG, GTT, GTC, GTA, GTG, TTT, TTC, ATG, TGT, TGC, GCT, \
GCC, GCA, GCG, GGT, GGC, GGA, GGG, CCT, CCC, CCA, CCG, ACT, ACC, ACA, ACG, TCT, TCC, TCA, TCG, AGT, AGC, TAT, TAC, TGG, \
CAA, CAG, AAT, AAC, CAT, CAC, GAA, GAG, GAT, GAC, AAA, AAG, CGT, CGC, CGA, CGG, AGA, AGG"
    codon_list = codon_string.split(', ')
    codon_list.sort()
    codon_map = {codon : 0 for codon in codon_list}
    return codon_map


#finds total count of each of the 61 codons in the list of codons of trimmed input orf sequences
def codon_counter(map, codon_list):
    for codon in map.keys():
        count = codon_list.count(codon)
        map[codon] = count
    return map

#takes updated dictionary of codon : count pairs and prints them to stdout with a tab between them
def tsv_printer(map, total):
    print(f"codon \t probability")
    for codon, count in map.items():
        print(f"{codon} \t {(count/total)}")



if __name__ == "__main__":
    dna_sequence, total_codons = orf_trimmer()
    codon_list_input = dna_input_separator(dna_sequence)
    codon_counter_map = getmap()
    codon_counter_map = codon_counter(codon_counter_map, codon_list_input)
    tsv_printer(codon_counter_map, total_codons)
    