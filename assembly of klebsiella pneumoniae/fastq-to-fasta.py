import sys
import fileinput





def fastq_to_fasta():
    #inputf = open(sys.argv[1], 'r') #opening input/output files                                                        
    #outputf = open(sys.argv[2], 'w')                                                                                   

    contig = ''
    quality = False
    counter = 0
    for line in fileinput.input():
        counter += 1
        line = line.strip()
        if line.startswith('+'):
            quality = True
            continue
        elif line.startswith('@'):
            if counter == 1:
                idq = line
                last_id =  '>' + idq[1:]
                continue
            quality = False
            idq = line
            id =  '>' + idq[1:]
            print(last_id)
            index = 0
            for chunk in range(0, len(contig), 80):
                index += 80
                print(contig[chunk:(chunk+80)])
            #print(contig, end= '')
            last_id = id
            contig = ''
        elif quality:
            continue
        else:
            contig += line
    print(id)
    print(contig, end= '')
            
            
            
            
            
if __name__ == "__main__":
    fastq_to_fasta()
