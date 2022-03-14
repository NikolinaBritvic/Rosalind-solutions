# Generate the d-Neighborhood of a String

def HammingDistance(text1,text2):
    count=0
    for i in range(len(text1)):
        if text1[i]!=text2[i]:
            count+=1
    return count

def Neighbors(pattern,d):
    if d==0:
        return {pattern};
    if len(pattern)==1:
        return {"A","C","G","T"}
    lista=set()
    SuffixNeighbors=Neighbors(pattern[1:],d)
    for text in SuffixNeighbors:
        if HammingDistance(pattern[1:],text)<d:
            for nt in ["A","C","G","T"]:
                lista.add(nt + text)
                

        else:
            lista.add(pattern[0] + text)
    return lista

pattern=input("Pattern: ")
d=int(input("d: "))
lista=Neighbors(pattern,d)
for el in lista:
    print(el)
            
