"Program to create metadata for biom file output from Fungene pipeline clustering step"
from collections import Counter
#Copy dist 0.0 clusters into a new file

clust_filename = input("Enter .clust filename:" )
#non_chimeric_prot_corr_aligned.fasta_1-13.clust
cluster =[]

with open(clust_filename, "r") as infile:
    for line in infile:
        if line[0].isdigit():
            x = line.rstrip('\n').split('\t')
            cluster.append(list(x))


framebot_filename = input('enter non_chimeric_framebot.txt file: ')
framebot = []
#non_chimeric_framebot_1-13.txt
with open(framebot_filename,'r') as infile:
    for line in infile:
        y = line.split('\t')
        framebot.append(y)

#pull out stats line from each entry
seq_taxa = []
for i in framebot:
    if "STATS" in i:
        seq_taxa.append(i[1:3])

#Match Cluster number to taxonomy
#formatting:
#Cluster# \t taxonomic lineage \t sequence id

data = []
for i in seq_taxa:
    for j in cluster:
        if i[1] in j[3]:
            data.append(j+i)


output_data = input("enter output file name: ")
with open(output_data, "w") as out_file:
    out_file.writelines('\t'.join(i) + '\n' for i in data)

