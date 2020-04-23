
#place accession numbers in a list
acc = input("Enter accesssion file: ")

accession = []

acc_file = open(acc, "r")
for line in acc_file:
    entry = line.rstrip('\n')
    accession.append(entry)

print(accession)

#input uniprot database file
uniprot_file = input("Enter Uniprot.dat file name: ")

uniprot = []
with open(uniprot_file) as inputfile:
    for line in inputfile:
        uniprot.append(line)

import itertools

w = '//\n'

new_uniprot = [[]]

for x,y in itertools.groupby(uniprot, lambda z: z==w):
    if x: new_uniprot.append([])
    new_uniprot[-1].extend(y)

uniprot = new_uniprot[1:]

uniprot_ent = []

for chunk in uniprot:
    print(chunk)
    #for z in chunk:
     #   print(z[1])
    for ac in accession:
        if ac in chunk[2]:#z:
            uniprot_ent.append(chunk)
        else:
            pass

#print(new_uniprot)
#print(uniprot_ent)
output = input("Enter output .dat file: ")
with open(output, "w") as out_file:
    out_file.writelines(''.join(i) + '\n' for i in uniprot_ent)