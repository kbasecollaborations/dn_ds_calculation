#!/usr/bin/python

import json

''' readinfg codon json'''
with open('json_data/codon.txt') as cf:
  codon_data = json.load(cf)
print(codon_data)

'''reading mutation codon'''
with open('json_data/mutation_codon.txt') as mcf:
  mutation_codon_data = json.load(mcf)
print(mutation_codon_data)

'''reading all possible path'''
with open('json_data/all_possible_path.txt') as appf:
  all_possible_path = json.load(appf)
print(all_possible_path)


def get_triplets(seq):
    codon_list = []
    for i in range(int(len(seq)/3)):
        start = 3*i
        end = 3*i+3
        codon_list.append(seq[start:end])
    return codon_list
    
seq = ''
with open("sample.fa") as fp:
    line = fp.readline()
    while line:
       if not line.startswith(">"):
          line = line.strip()
          seq = seq + line
       line = fp.readline()

codonlist = get_triplets(seq)


'''Calculating N and S for reference genome '''
N = 0
S = 0

for codon in codonlist:
    N1 = mutation_codon_data[codon+"_N_1"]
    N2 = mutation_codon_data[codon+"_N_2"]
    N3 = mutation_codon_data[codon+"_N_3"]
    S1 = mutation_codon_data[codon+"_S_1"]
    S2 = mutation_codon_data[codon+"_S_2"]
    S3 = mutation_codon_data[codon+"_S_3"]    
    N = N + (N1 + N2 + N3)
    S = S + (S1 + S2 + S3)

print(N)
print(S)



'''Calculating Nd and Sd for input vcf file
with open("input.vcf") as fvp:
    vcfline = fvp.readline()
    while vcfline:
       if not vcfline.startswith("#"):
          vcfline = vcfline.strip()
       fine = fvp.readline()
'''
