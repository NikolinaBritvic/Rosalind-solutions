# Implement NumberToPattern

def NumberToPattern(index, k):
    pattern = list()
    D = {0: "A", 1: "C", 2: "G", 3: "T"}
    q = index
    for i in range(0, k):
        r = q % 4
        q = q // 4
        pattern.append(D[r])
    return "".join(pattern[::-1])

index=int(input("Index: "))
k=int(input("k: "))
print(NumberToPattern(index,k))
