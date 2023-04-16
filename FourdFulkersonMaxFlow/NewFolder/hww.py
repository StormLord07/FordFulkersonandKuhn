from collections import deque

points = [[0, 2], [2, 5], [5, 2], [6, 6], [8, 3]]
distance = [[] for i in range(0, len(points))]

q = deque()
q.append(0)

for j in range(0, len(points)):
    for i in range(0, len(points)):
        distance[j].append(((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5)
    distance[j] = list(enumerate(distance[j], 0))
    for i in range(0, len(distance[j])):
        if distance[j][i][1] == 0:
            distance[j].pop(i)
            break
dictionary = {}
for i in range(0, len(distance)):
    dictionary[i] = distance[i]


furthest = max(dictionary[0], key=lambda i: i[1])[0]
q.append(furthest)
dictionary.pop(0)
nearest = min(dictionary[furthest], key=lambda i: i[1])[0]
dictionary.pop(furthest)


while len(q) != len(points):

    for i in dictionary.keys():
        temp = len(dictionary[i])
        j=0
        while j < temp:
            if dictionary[i][j][0] in q:
                dictionary[i].pop(j)
                temp-=1
            j+=1
    for i in q:
        if i in dictionary.keys():
            dictionary.pop(i)
    q.append(nearest)
    if len(dictionary)==1:
        break
    nearest = min(dictionary[nearest], key=lambda i: i[1])[0]
print(q)

q.append(0)
prev = q.popleft()
temp = prev
string = str(points[prev]) + "->"
while q:
    prev = temp
    temp=q.popleft()
    string += str(points[temp]) + str(((points[temp][0] - points[prev][0]) ** 2 + (points[temp][1] - points[prev][1]) ** 2) ** 0.5) + '->'

print(string.strip('->'))