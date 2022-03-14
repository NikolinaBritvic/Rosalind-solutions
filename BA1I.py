from collections import defaultdict

def neighbour(pattern, mismatch, words):
    bases = ['A', 'T', 'G', 'C']
    for i in range(len(pattern)):
        for j in range(len(bases)):
            new_pattern = pattern[:i] + bases[j] + pattern[i+1:]
            if mismatch <= 1:
                words.add(new_pattern)
            else:
                neighbour(new_pattern, mismatch - 1, words)
def FindMostFrequentWords(text, k, d):
    AllFrequentWords = defaultdict(int)
    for i in range(len(text) - k + 1):
        FrequentWords = set()
        neighbour(text[i:i + k], d, FrequentWords)
        for words in FrequentWords:
            AllFrequentWords[words] += 1
    # print AllFrequentWords
    for t in AllFrequentWords.keys():
        if AllFrequentWords[t] == max(AllFrequentWords.values()):
            print(t, end=" ")

text=input("Unesi text: ")
k=int(input("Unesi k: "))
d=int(input("Unesi d: "))
print(FindMostFrequentWords(text,k,d))
