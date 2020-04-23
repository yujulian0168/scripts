import sys
id_file = sys.argv[sys.argv.index('-i')+1]
uniprot_file = sys.argv[sys.argv.index('-u')+1]
out_file = sys.argv[sys.argv.index('-o')+1]

import csv

# Begin by importing matches-accession ID file and creating lists of sample information.

def import_file(filename, separator):
    for line in csv.reader(open(filename), delimiter=separator, skipinitialspace=True):
        if line:
            yield line


AC = [ ]  # column 1 is entry ID of the matches-id file
ID = [ ]  # column 2 is accession number of the matches-id file

for row in import_file(id_file, '\t'):
    AC.append(row[0])
    ID.append(row[1])

#for x in AC:
#    print(x)

#for i in ID:
#    print(i)

import itertools
uniprot = [ ]

with open(uniprot_file) as inputfile:
    for line in inputfile:
        uniprot.append(line)

#for i in uniprot:
#    print(i)

w = '//\n'

spl = [[]]
for x,y in itertools.groupby(uniprot, lambda z: z==w):
    if x: spl.append([])
    spl[-1].extend(y)

#print(spl)

#print(ID)

uniprot_ent = [ ]

ID_counter = 0

for chunk in spl:
    for z in chunk:
        for id in ID:
            ID_counter += 1
            if ID_counter % 1000 == 0:
                print(str(ID_counter))
            if id in z:
                print(id)
                uniprot_ent.append(chunk)
            else:
                pass

#print(uniprot_ent)



#uniprot_ent_output1 = open("/Users/julian/Desktop/BIOCHAR/3_Biochar_Metagenomics/BC2/uniprot/uniprot_ent_output1.dat", "w")
with open(out_file, "w") as file:
    file.writelines(''.join(i) + '\n' for i in uniprot_ent)

#for i in uniprot_ent:
#    for y in i:
#        print(y)

