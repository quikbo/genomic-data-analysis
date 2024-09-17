Explanation of how to produce final annotation file and how program works:

In the directory of this text file, hw2q1d, exists the program that 
generates the final gtf file. This program is called hw2q1d.py. 

The input should follow this form:
python3 annotation.py <gtf file> <mummer alignment file> <known proteins faa file> <output final gtf annotation file name>

Note that output will be in gtf format 


The way this program works is by first making a name map of key value pairs where the key is 
the accession number and value is the protein's name. This information is found in the known proteins file 
and is used in the final column of gtf output whenever there is a matched gene. Then the program makes an
orf map that makes the orf number the key and the accession number the value for all the matches in 
the mummer file. This map is used for 1. seeing if the orfs from the prediction gtf file matched any of
the alignments and 2. for easily obtaining an orf's accession number which can then be used to 
access the protein's name using the first map.

Once the two maps are created, the program then loops through every line of the prediction gtf file. 
It extracts out the orf number in each line and if that orf is in the orf map, that means it matched 
a gene and then the accession number and the protein name information is included in the final annotation output file.
If it doesn't match a gene, match is set to none and protein name is left blank in output file. 