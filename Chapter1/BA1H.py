# Find All Approximate Occurrences of a Pattern in a String

def HammingDistance(text1,text2):
    count=0
    for i in range(len(text1)):
        if text1[i]!=text2[i]:
            count+=1
    return count

def FindOccurrences(pattern,text,d):
    lista=[]
    ln=len(pattern)
    for i in range(len(text)-ln+1):
        if HammingDistance(text[i:(i+ln)],pattern)<=d:
            lista.append(i)
    return lista
        

pattern=input("Unesi pattern: ")
text=input("Unesi text: ")
d=int(input("Unesi d: "))
print(FindOccurrences(pattern,text,d))
