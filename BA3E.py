# Construct the De Bruijn Graph of a Collection of k-mers

def DeBruijn2(text):
    rez={}
    for row in text:
        node=row[:-1]
        if node not in rez.keys():
            rez[node]=[row[1:]]
        else:
            rez[node].append(row[1:])
    return rez

unos='''GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG'''
unos=unos.splitlines()
rez=DeBruijn2(unos)

for key in sorted(rez):
    ispis=''
    for i in range(len(rez[key])):
        if(i==(len(rez[key])-1)):
            ispis+=rez[key][i]
        else:
            ispis+=rez[key][i]+","
    print(key+" -> "+ispis)
