# Generate the d-Neighborhood of a String

from itertools import product

def allKmers(k):
    return [''.join(i) for i in product('ACGT', repeat = k)]

def HammingDistance(text1,text2):
    count=0
    for i in range(len(text1)):
        if text1[i]!=text2[i]:
            count+=1
    return count

def Metoda(text,d):
    kmeri=allKmers(len(text))
    lista=[]
    for kmer in kmeri:
        if HammingDistance(kmer,text)<=d:
            if kmer not in lista:
                lista.append(kmer)
    for i in range(len(lista)):
        print(lista[i])

text=input("text: ")
d=int(input("d: "))
Metoda(text,d)
