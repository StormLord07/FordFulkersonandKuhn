import math

with open("test" + str(input()) + ".in") as f:
  G = f.readlines()
  for i in range(0, len(G)):
    G[i] = G[i].strip().split(" ")
    for j in range(0, len(G[i])):
      G[i][j] = int(G[i][j])
      if i-1 != j and G[i][j] == 0:
        G[i][j]=math.inf

E = G.pop(0).pop(0)


