g = []
with open(str(input() + ".in")) as f:
    for line in f:
        g.append([int(x) for x in line.split()])


def kuhn(x):
    if used[x]:
        return False
    used[x] = True
    for i in range(1, len(g[x])):
        if g[x][0] == 0:
            break
        to = g[x][i]
        if mt[to] == -1 or kuhn(mt[to]):
            mt[to] = x
            return True
    return False


n, k = g[0][0], g[0][1]
g.pop(0)
print(g)
mt = [-1] * k


for j in range(0, n):
    used = [False] * n
    kuhn(j)


answer=0
for i in range(0, k):
    if mt[i] != -1:
        answer+=1
print(answer)