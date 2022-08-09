# Find the Length of a Longest Path in a Manhattan-like Grid

def ManhattanTourist(n, m, down, right):
    
    s = []
    for i in range(n + 1):
        s.append((m + 1) * [0])

    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + down[i - 1][0]

    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] + right[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1])

    return s[n][m]


unos = '''4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2'''

unos=unos.splitlines()
n=unos[0].split()[0]
m=unos[0].split()[1]

down = []
for i in range(int(n)):
    down.append([int(x) for x in unos[1 + i].split()])

right = []
for i in range(int(n) + 1):
    right.append([int(x) for x in unos[int(n) + 2 + i].split()])

res = ManhattanTourist(int(n), int(m), down, right)

print(str(res))
