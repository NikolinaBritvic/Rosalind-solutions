# Compute the Hamming Distance Between Two Strings

def HammingDistance(text1,text2):
    count=0
    for i in range(len(text1)):
        if text1[i]!=text2[i]:
            count+=1
    return count

text1=input("Unesi prvi text: ")
text2=input("Unesi drugi text: ")
print(HammingDistance(text1,text2))
