# Computing a Frequency Array
from itertools import product

def allKmers(k):
    return [''.join(i) for i in product('ACGT', repeat = k)]
    
def Metoda(text,k):
    kmeri=allKmers(k)
    arr=[0]*len(kmeri)   
    for i in range(len(kmeri)):
        br=0 
        for j in range(len(text)-k+1):
            if text[j:j+k]==kmeri[i]:
                br+=1
            arr[i]=br
    s=""
    for i in range(len(arr)):
        s+=str(arr[i])+" "
    return s
        

text=input("Text: ")
k=int(input("k: "))
print(Metoda(text,k))

