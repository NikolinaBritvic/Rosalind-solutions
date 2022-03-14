# Find the Most Frequent Words in a String

def kmer(text,i,k):
    return text[i:(i+k)];

def MostFrequent(text,k):
    counts={}
    for i in range(len(text)-k+1):
        if text[i:(i+k)] not in counts:
            counts[text[i:(i+k)]]=0
        counts[text[i:(i+k)]]+=1
    max_count=max(counts.values())
    for name,count in counts.items():
        if count==max_count:
            print(name)
    return max_count

text=input("Unesi tekst: ")
k=int(input("Unesi k : "))
MostFrequent(text,k)
    
