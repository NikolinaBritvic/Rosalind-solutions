# Implement DistanceBetweenPatternAndStrings

import math

def HD(a,b):
    
  hd=0
  
  for i in range(0,len(a)):
    if a[i]!=b[i]:
      hd+=1
      
  return hd

def Distance(Pattern, Dna):
    
  k=len(Pattern)
  distance=0

  for Text in Dna:
      hd=math.inf
      for i in range(0,len(Text)-k):
          kmer=Text[i:i+k]
          if hd>HD(Pattern, kmer):
              hd=HD(Pattern, kmer)
      distance+=hd
  return distance

unos='''AAA
TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT'''
pattern=unos.splitlines()[0]
niz_dna=unos.splitlines()[1].split(" ")

print(Distance(pattern,niz_dna))
