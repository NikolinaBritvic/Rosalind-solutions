# Generate the k-mer Composition of a String

def Composition(text,k):
    lista=[]
    for i in range(len(text)-k+1):
        lista.append(text[i:i+k])
    lista=sorted(lista)
    for el in lista:
        print(el)


unos_='''5
CAATCCAAC'''
unos=unos_.splitlines()
k=int(unos[0])
text=unos[1]

Composition(text,k)


