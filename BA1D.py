# Find All Occurrences of a Pattern in a String

def Occurrences(pattern,text):
    ln=len(pattern)
    for i in range(len(text)-ln+1):
        if text[i:(i+ln)]==pattern:
            print(i)

pattern=input("Unesi pattern: ")
text=input("Unesi text: ")
Occurrences(pattern,text)
