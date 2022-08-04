# Construct the De Bruijn Graph of a String

def DeBruijn(text,k):
    rez={}
    for i in range(len(text)-k+1):
        node=text[i:i+k-1]
        if node not in rez.keys():
            rez[node]=[text[i+1:i+k]]
        else:
            rez[node].append(text[i+1:i+k])
    return rez

unos='''4
AAGATTCTCTAC'''
unos=unos.splitlines()
k=int(unos[0])
text=unos[1]

rez=DeBruijn(text,k)
for key in sorted(rez):
    ispis=''
    for i in range(len(rez[key])):
        if(i==(len(rez[key])-1)):
            ispis+=rez[key][i]
        else:
            ispis+=rez[key][i]+","
    print(key+" -> "+ispis)
