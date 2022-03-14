# Find a Position in a Genome Minimizing the Skew

def Minimaze(text):
    lista=[0]
    for i in range(len(text)):
        if text[i]=="G":
            lista.append(lista[-1]+1)
        elif text[i]=="C":
            lista.append(lista[-1]-1)
        else:
            lista.append(lista[-1])
    minimum=min(lista)
    for i in range(len(lista)):
        if lista[i]==minimum:
            print(i)
    return lista
    
text=input("Unesi text: ")
Minimaze(text)
