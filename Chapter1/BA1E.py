# Find Patterns Forming Clumps in a String

def FindClumps(text,k,L,t):
    lista=[]
    for i in range(len(text)-L+1):
        for j in range(i,i+L-k):
            if text[i:i+L].count(text[j:(j+k)])==t:
                lista.append(text[j:(j+k)])
    lista=set(lista)
    return lista

text=input("Unesi text: ")
k=int(input("Unesi k: "))
L=int(input("Unesi L: "))
t=int(input("Unesi t: "))

print(FindClumps(text,k,L,t))
