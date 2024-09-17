import sys

#takes the known alignment file and maps the accession number as key to the protein name as its value in a dictionary
def getNAMEmap():
    with open(sys.argv[3], 'r') as known_alignment:
        map = {}
        for line in known_alignment:
            if line[0] == '>':
                fields = line.split()
                accession = fields[0][1:15] #extracting accession number 
                protein_name_list = fields[1:-2] #omitting accession and genus
                if fields[-2][0] != '[':
                    protein_name_list.append(fields[-2]) #had to make this conditional due to multi name genuses 
                protein_name = ' '.join(protein_name_list)
                map[accession] = protein_name
        return map





#figure out situation where multiple ORFs align to same protein
#this is actually being done incorrectly with the counter method, figure something else out 
#06723, **25 ** 26 **27 all need to match to WP_023279041.1 in final annotation, as an example of this
#i think making a list of orfs to be added could work, update: this worked 

#after office hours, realized that orf lines not followed by accession number don't have matches

#takes the mummer alignment file and maps the orfs to accession number in a dictionary
def getORFmap():
    with open(sys.argv[2], 'r') as mummer:
        map = {}
        line = mummer.readline()
        counter = 0
        while True:
            if line == "":
                break
            elif line[0] == '>':
                orf_line = line
                next = mummer.readline()
                if next[0] == '>': #if an orf line follows an orf line, skips and goes through loop again
                    line = next
                    continue
                else:
                    orf = orf_line.split()[1]
                    accession = next.split()[0]
                    map[orf] = accession
                    line = mummer.readline()
            else:
                line = mummer.readline()
                continue #for cases with multiple accession numbers
            
        """
        orf_list = []
        for line in mummer:
            if line[0] == '>':
                fields = line.split()
                orf_list.append(fields[1])
            else: #now we have reached an informational line with accession number
                fields = line.split()
                accession = fields[0] #extract accession number
                for orf in orf_list: #for all the orfs that preceded this informational line, append to dictionary
                    map[orf] = accession
                orf_list.clear() #empty list for the next orf, accession pairs to be added
        """
        return map



def alignment_to_final_gtf():
    with open(sys.argv[1], 'r') as gtf_in, open(sys.argv[4], 'w') as out:
        accession_to_name_map = getNAMEmap()
        orf_to_accession_map = getORFmap()
        counter = 0
        for line in gtf_in:
            counter += 1
            final_gtf_fields = line.split()
            transcript_id = final_gtf_fields[-1][1:-1] #extracting orf number
            final_gtf_fields[1] = transcript_id #replacing "glimmer3" with the orf number
            #have to edit how we access mummer file orf's because they are not in ascending order
            if transcript_id in orf_to_accession_map:
                accession = orf_to_accession_map[transcript_id]
                final_gtf_fields[-2] = f"match={accession}"
                final_gtf_fields[-1] = accession_to_name_map[accession]
            else: #if they don't match
                final_gtf_fields[-2] = "match=none" #match will be none
                final_gtf_fields[-1] = '' #setting protein name to a blank

            final_gtf_fields[3] = final_gtf_fields[3].ljust(10) #adjusting format
            final_gtf_fields[4] = final_gtf_fields[4].ljust(10)
            final_gtf_string = '\t'.join(final_gtf_fields)
            out.write(f"{final_gtf_string}\n")



if __name__ == "__main__":
    alignment_to_final_gtf()