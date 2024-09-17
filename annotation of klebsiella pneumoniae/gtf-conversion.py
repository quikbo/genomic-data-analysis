import sys



def glimmer_to_gtf():
    with open(sys.argv[1], 'r') as inf, open(sys.argv[2], 'w') as out:
        header_fields = inf.readline().split()
        name = header_fields[0].replace('>', '') #extracting name from FASTA header
        for line in inf:
            fields = line.split() #turn a line from predict file into a list for easy extractions
            frame = fields[3][0]
            start = str(fields[1]) #extracting start position
            stop = str(fields[2]) #extracting end position
            if frame == '-': #swapping start and stop for negative reading frames
                start, stop = stop, start
            id = f"transcript_id \"{fields[0]}\"" #creating string with id attribute for last field of gtf format
            gtf_fields = [name, "glimmer3", "CDS", start, stop, ".", frame, ".", id]
            gtf_fields_string = '\t'.join(gtf_fields) #combine gtf fields list into a string to be written 
            out.write(f"{gtf_fields_string}\n")


if __name__ == "__main__":
    glimmer_to_gtf()