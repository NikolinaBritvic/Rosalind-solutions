# Generate the Convolution of a Spectrum

def Convolution(s):
    l=[]
    
    for a in s:
        for b in s:
            if a-b>0:
                l.append(a-b)
                
    for i in range (len(l)):
        l[i]=str(l[i])
        
    l.sort()
    return " ".join(l)
  
unos="0 137 186 323"
unos=unos.split(" ")
unos=[int(br) for br in unos]

print(Convolution(unos))


