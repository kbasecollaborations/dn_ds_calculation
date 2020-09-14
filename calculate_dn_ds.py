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

print(get_triplets(seq))

