

infile = open("id_test.txt", "r")

api = []
api_all = []

for i in infile:
    id = i.rstrip('\n')
    api.append("http://api.metagenomics.anl.gov//m5nr/md5/" + id + "?source=KO&version=10")
    api_all.append("http://api.metagenomics.anl.gov//m5nr/md5/" + id + "?version=10")

#print(api)
output = input("Enter output file for api file: ")
with open(output, "w") as out_file:
   out_file.writelines(''.join(i) + '\n' for i in api)

#print(api_all)
output_all = input("Enter output file for api_all file: ")
with open(output_all, "w") as out_file_2:
    out_file_2.writelines(''.join(j) + '\n' for j in api_all)