# Reconstruct a String from its Genome Path

def Reconstruction(text):
    res=text[0]
    for row in text[1:]:
        res+=row[-1]
    return res

unos_='''ACCGA
CCGAA
CGAAG
GAAGC
AAGCT'''

unos=unos_.splitlines()
print(Reconstruction(unos))
