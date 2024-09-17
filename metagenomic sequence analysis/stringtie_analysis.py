import sys


def gtf_analyzer_stringtie():
    with open("stringtie_merged.gtf", "r") as f:
        lines = f.readlines()
        transcript_count = 0
        gene_ids = set()
        for line in lines:
            if line == '':
                break
            fields = line.split()
            if fields[1] == "Curated":
                classification = fields[3]
                gene_id = fields[10][1:-2]
            else:
                classification = fields[2]
                gene_id = fields[9][1:-2]
            gene_ids.add(gene_id)
            if classification == "transcript":
                transcript_count += 1

        print(f"transcript count: {transcript_count}")
        print(f"distinct genes: {len(gene_ids)}")
    



def gtf_analyzer_annotation():
    with open("CHESS_v3.0_chr17.gtf", "r") as f:
        lines = f.readlines()
        transcript_count = 0
        transcript_PC_count = 0
        gene_id_dict = {}
        for line in lines:
            if line == '':
                break
            fields = line.split()

            if fields[1] == "Curated":
                classification = fields[3]
                gene_id = fields[12][1:-2]
            else:
                classification = fields[2]
                gene_id = fields[11][1:-2]

            if len(fields) > 13: #contains gene type info
                for i in range(10, len(fields)):
                    if fields[i] == "gene_type":
                        i += 1
                        gene_id_dict[gene_id] = fields[i] #setting value of id to be its type
                        if classification == "transcript":
                            transcript_count += 1
                            if fields[i][1:-2] == "protein_coding":
                                transcript_PC_count += 1
            else:
                if gene_id not in gene_id_dict:
                    gene_id_dict[gene_id] = '' #adding any distinct genes that don't have type info
        
        protein_coding_count = 0
        for id, type in gene_id_dict.items():
            if type[1:-2] == "protein_coding":
                protein_coding_count += 1

        print(f"total transcript count: {transcript_count}")
        print(f"protein coding transcript count: {transcript_PC_count}")
        print(f"distinct genes: {len(gene_id_dict)}")
        print(f"distinct protein coding genes: {protein_coding_count}")






if __name__ == "__main__":
    print("Stringtie_merged")
    gtf_analyzer_stringtie()
    print()
    print("Chr17")
    gtf_analyzer_annotation()
   # gtf_analyzer_annotation()