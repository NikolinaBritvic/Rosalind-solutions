# Implement CycleToChromosome

def CycleToChromosome(cycle):
    
    chromosome = []
    for i in range(0, len(cycle), 2):
        if cycle[i] < cycle[i + 1]:
            chromosome.append(cycle[i + 1] // 2)
        if cycle[i] > cycle[i + 1]:
            chromosome.append(-1 * cycle[i] // 2)
            
    return chromosome

def f(x):
    if x >= 0:
        return f"+{x}"
    else:
        return f"{x}"

unos="(1 2 4 3 6 5 7 8)"
unos=[int(x) for x in unos[1:-1].split(" ")]

res = CycleToChromosome(unos)
print("(" + " ".join([f(x) for x in res]) + ")")
