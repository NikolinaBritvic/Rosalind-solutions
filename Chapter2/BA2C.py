# Find a Profile-most Probable k-mer in a String

def kmers(text,L):
    """list of all L-windows in text"""
    windows=list()
    for i in range (0,len(text)-L+1):
        windows.append(text[i:(i+k)])
    #print(windows)
    return windows

def probability(window,profile):
    # probability of kmer in string according to profile matrix
    prob=1
    for i in range (0,len(window)):
        if window[i]=='A':
            prob=prob*profile[0][i]
        elif (window[i]=='C'):
            prob = prob * profile[1][i]
        elif (window[i] == 'G'):
            prob = prob * profile[2][i]
        else:
            prob = prob * profile[3][i]

    return prob

def profile_most_probable(text,k,profile):
    d=dict()
    for window in kmers(text,k):
        d[window]=probability(window,profile)
    return  [x[0] for x in d.items() if x[1]==max(d.values())][0]


x = '''CGCCCGTGAATCGGCCGCTAATGTGTCAGGCCCAGCGGCTGCCTCGCCTGGTATAAAACTGCTACGTCATGCGGGAACCGTCGGAGGAGTTCACCGTATCGTGTAGCCAATAACTATCCGTTTGTTTCGCATCAAGTCTCGTATTAAGGATCACCAGATCTAAAATCGAGAGCAGCCTAGTTTCCAATGGCCGCAAGGAT
6
0.242 0.152 0.121 0.333 0.303 0.242
0.182 0.303 0.303 0.364 0.242 0.212
0.152 0.242 0.212 0.152 0.121 0.242
0.424 0.303 0.364 0.152 0.333 0.303
'''
inlines=x.split('\n')
text=inlines[0]
k=int(inlines[1])
profile=list()
for i in range(2,6):
    profile.append(inlines[i].split())
    for j in range(0, k):
        profile[i-2][j] = float(profile[i-2][j])
res=profile_most_probable(text,k,profile)
print(res)










    
