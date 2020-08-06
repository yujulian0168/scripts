# This program matches the acc id from the repseq.fasta and original fasta and creates a new file with only matching seqeunces
from Bio import SeqIO

fasta_filtered = []

for seq_record_repseq in SeqIO.parse("all_aln_seqs_derep_representatives.fasta", "fasta"):
    for seq_record_fasta in SeqIO.parse("all_seqs_derep.fasta", "fasta"):
        if seq_record_repseq.id in seq_record_fasta.id:
            #print(seq_record_fasta.format("fasta"))
            fasta_filtered.append(seq_record_fasta)



print(fasta_filtered)

SeqIO.write(fasta_filtered, "acdS-filtered-refseq.fasta", "fasta")
