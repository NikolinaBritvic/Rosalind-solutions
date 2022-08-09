# Implement ChromosomeToCycle

def ChromosomeToCycle(chromosome):
    
    cycle = []
    
    for x in chromosome:
        if x > 0:
            cycle.extend([2 * x - 1, 2 * x])
        if x < 0:
            x = abs(x)
            cycle.extend([2 * x, 2 * x - 1])
            
    return cycle

unos="(+1 -2 -3 +4)"
unos=[int(x) for x in unos[1:-1].split(" ")]

res = ChromosomeToCycle(unos)
print( "(" + " ".join([str(x) for x in res]) + ")" )
