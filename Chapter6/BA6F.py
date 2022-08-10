# Implement ChromosomeToCycle

def ChromosomeToCycle(chromosome):
    
    cycle = []
    for j in range(len(chromosome)):
        i=int(chromosome[j])
        if i > 0:
            cycle.append(2 * i - 1)
            cycle.append(2 * i )
        else:
            cycle.append(-2 * i )
            cycle.append(-2 * i - 1)
            
    return cycle

unos="(+1 -2 -3 +4)"
unos=[int(x) for x in unos[1:-1].split(" ")]

res = ChromosomeToCycle(unos)
print( "(" + " ".join([str(x) for x in res]) + ")" )
