# Frequent Words with Mismatches and Reverse Complements Problem

from itertools import product

def HammingDistance(a,b):
    br=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            br+=1
    return br

def ReverseComplement(a):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in a[::-1]])

def kmeri(k):
    kmers=["".join(c) for c in product("ACGT",repeat=k)]
    return kmers

def Metoda(text,k,d):
    lista={}
    kmers=kmeri(k)
    
    for kmer in kmers:
        for i in range(len(text)-k+1):
            if HammingDistance(text[i:i+k],kmer)<=d:
                if kmer not in lista:
                    lista[kmer]=1
                else:
                    lista[kmer]+=1
            if HammingDistance(text[i:i+k],ReverseComplement(kmer))<=d:
                if kmer not in lista:
                    lista[kmer]=1
                else:
                    lista[kmer]+=1
    
    max_=max(lista.values())
    result=[]
    for name,value in lista.items():
        if value==max_:
            result.append(name)
    return result

text=input("Text: ")
k=int(input("k: "))
d=int(input("d: "))
print(Metoda(text,k,d))


