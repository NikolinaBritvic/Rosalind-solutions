# Implement PatternToNumber

def SymbolToNumber(symbol):
    if symbol=="A":
        return 0;
    elif symbol=="C":
        return 1;
    elif symbol=="G":
        return 2;
    elif symbol=="T":
        return 3;

def PatternToNumber(dna):
    if len(dna)==0:
        return 0
    symbol=dna[-1] # zadnji simbol
    prefix=dna[:-1] # prvi simbol
    res=4*PatternToNumber(prefix) + SymbolToNumber(symbol)
    return res
    

dna=input("Unesi dna: ")
print(PatternToNumber(dna))
