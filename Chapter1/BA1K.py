# Computing a Frequency Array

from itertools import product

def allKmers(k):
    return [''.join(i) for i in product('ACGT', repeat = k)]

def countKmer(dna, kmer):
    count = 0
    for i in range(len(dna) - len(kmer) + 1):
        if dna[i : i + len(kmer)] == kmer:
            count += 1
    return(count)

def FrequencyArray(text,k):
    kmers = allKmers(k)
    freq = [0] * len(kmers)
    for i in range(len(kmers)):
        freq[i] = countKmer(text, kmers[i])
    return ' '.join([str(x) for x in freq])

text=input("Unesi text: ")
k=int(input("Unesi k: "))
print(FrequencyArray(text,k))
