# Implement NumberToPattern

def NumberToSymbol(s):
  if (s==0):
    return "A"
  elif (s==1):
    return "C"
  elif (s==2):
    return "G"
  else:
    return "T"
    
    
def NumberToPattern(index,k):
  if(k==1):
    return NumberToSymbol(index)
  q=index//4
  r=index%4
  s=NumberToSymbol(r)
  prefixPattern=NumberToPattern(q,k-1)
  return  prefixPattern+s

index=int(input("Index: "))
k=int(input("k: "))
print(NumberToPattern(index,k))
