# Construct the Overlap Graph of a Collection of k-mers

def Prefix(text):
    return text[:-1]

def Sufix(text):
    return text[1:]

def OverlapGraph(text):
    rez={}
    for row in text:
        for row1 in text:
            if Sufix(row)==Prefix(row1):
                if row not in rez.keys():
                    rez[row]=[row1]
                else:
                    rez[row].append(row1)
    return rez

unos='''ATGCG
GCATG
CATGC
AGGCA
GGCAT'''

unos=unos.splitlines()
rez=OverlapGraph(unos)
for key in sorted(rez):
    for value in rez[key]:
        print(key+" -> "+value)
