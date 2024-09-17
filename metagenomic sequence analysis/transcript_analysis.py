import sys

def annotation_gene_id_type_dict():
    with open("CHESS_v3.0_chr17.gtf", "r") as f:
        lines = f.readlines()
        gene_id_dict = {}
        for line in lines:
            if line == '':
                break
            fields = line.split()

            if fields[1] == "Curated":
                gene_id = fields[12][1:-2]
            else:
                gene_id = fields[11][1:-2]

            if len(fields) > 13: #contains gene type info
                for i in range(10, len(fields)):
                    if fields[i] == "gene_type":
                        i += 1
                        gene_id_dict[gene_id] = fields[i] #setting value of id to be its type
            else:
                if gene_id not in gene_id_dict:
                    gene_id_dict[gene_id] = '' #adding any distinct genes that don't have type info
    return gene_id_dict


def tmap_analyzer():
    gene_id_type_dict = annotation_gene_id_type_dict()

    with open("merged.stringtie_merged.gtf.tmap", "r") as f:
        lines = f.readlines()
        exact_matches = 0
        novel_j = 0
        novel_u = 0

        for line in lines:
            if line == '':
                break
            fields = line.split()

            code = fields[2]
            gene_id = fields[0]

            if code == '=': #2a
                exact_matches += 1
            elif code == 'u': #2c
                novel_u += 1
            
            if code != '=': #2b
                if gene_id in gene_id_type_dict:
                    if gene_id_type_dict[gene_id][1:-2] == "protein_coding":
                        novel_j += 1

        print(f"exact transcript matches count: {exact_matches}")
        print(f"novel transcripts in protein-coding gene loci: {novel_j}")
        print(f"novel transcripts in novel locations: {novel_u}")



if __name__ == "__main__":
    tmap_analyzer()
