import sys



def tpm_analysis():
    highest_tpm_sample = ''
    highest_tpm = 0
    highest_tpm_record = ''

    distinct_transcripts_tpms = {} #dict key: transcript_id, value: TPM
    distinct_genes_tpms = {}
    maxtpm_transcripts = {}

    for line in sys.stdin: #stdin is file with names of 11 samples one on each line
        with open(line.strip(), "r") as f: #opens each of the 11 samples and goes through it
            lines = f.readlines()
            highest_tpm_infile = 0
            highest_tpm_record_infile = ''
            for record in lines:
                if record == '':
                    break
                fields = record.split()
                if fields[2] == "transcript" or fields[3] == "transcript":
                    tpm = float(fields[-1][1:-2])

                    if fields[1] == "Curated":
                        transcript_id = fields[12][1:-2]
                        gene_id = fields[10][1:-2]
                    else:
                        transcript_id = fields[11][1:-2]
                        gene_id = fields[9][1:-2]

                    if tpm > highest_tpm_infile:
                        highest_tpm_infile = tpm
                        highest_tpm_record_infile = record

                    if transcript_id not in distinct_transcripts_tpms:
                        distinct_transcripts_tpms[transcript_id] = tpm
                    
                    if gene_id not in distinct_genes_tpms:
                        distinct_genes_tpms[gene_id] = tpm
                    
                    if transcript_id in maxtpm_transcripts.keys():
                        if tpm > maxtpm_transcripts[transcript_id]:
                            maxtpm_transcripts[transcript_id] = tpm
                    else:
                        maxtpm_transcripts[transcript_id] = tpm

        if highest_tpm_infile > highest_tpm:
            highest_tpm_sample = line.strip()
            highest_tpm = highest_tpm_infile
            highest_tpm_record = highest_tpm_record_infile
    
    print("a")
    print(f"Sample with the highest TPM: {highest_tpm_sample}")
    print(f"TPM: {highest_tpm}")
    print(highest_tpm_record)

    nonzero_tpm_transcript_count = 0
    for id, tpm in distinct_transcripts_tpms.items():
        if tpm > 0:
            nonzero_tpm_transcript_count += 1

    print("b")
    print(f"distinct transcripts: {len(distinct_transcripts_tpms)}")
    print(f"distinct transcripts with tpm > 0: {nonzero_tpm_transcript_count}")
    print() 
    nonzero_tpm_gene_count = 0
    for id, tpm in distinct_genes_tpms.items():
        if tpm > 0:
            nonzero_tpm_gene_count += 1

    print("c")
    print(f"distinct genes: {len(distinct_genes_tpms)}")
    print(f"distinct genes with tpm > 0: {nonzero_tpm_gene_count}")
    print()

    maxtpm50_count = 0
    for id, count in maxtpm_transcripts.items():
        if count > 50:
            maxtpm50_count += 1


    print("d")
    print(f"distinct transcripts with MAX tpm > 50: {maxtpm50_count}")
    print()




def total_expression_analysis(lines):
    expression_dict = {}
    for line in lines:
        fields = line.split()
        if len(fields) > 10:
            if fields[1] == "Curated":
                gene_id = fields[10][1:-2]
            else:
                gene_id = fields[9][1:-2]
            tpm = 0.0
            if fields[-1][0] == '"':
                tpm = float(fields[-1][1:-2])
            if gene_id in expression_dict:
                expression_dict[gene_id] += tpm
            else:
                expression_dict[gene_id] = tpm
    return sorted(expression_dict.items(), key = lambda item: item[1], reverse= True)

def partE():
    with open("a479052_reestimate.gtf", "r") as f:
        lines = f.readlines()
        expression_dict52 = total_expression_analysis(lines)
        for i in range(10):
            print(f"{i+1}. {expression_dict52[i]}")


    with open("a479054_reestimate.gtf", "r") as f:
        lines = f.readlines()
        expression_dict54 = total_expression_analysis(lines)
        for i in range(10):
            print(f"{i+1}. {expression_dict54[i]}")




if __name__ == "__main__":
    tpm_analysis()
    partE()