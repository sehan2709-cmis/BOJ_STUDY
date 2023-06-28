n, m, v = map(int, input().split())

graph = [[0 for x in range(n)] for y in range(n)]

for i in range(m):
  x, y = map(int, input().split())
  graph[x - 1][y - 1] = 1
  graph[y - 1][x - 1] = 1

#dfs
dfsVisit = [0 for x in range(n)]
visitOrder = 1
dfsVisit[v-1] = visitOrder
print(v, end = " ")
index = v-1
while(1):
  found = 0
  for i in range(n):
    if dfsVisit[i] == 0 and graph[index][i] == 1:
      visitOrder += 1
      index = i
      dfsVisit[i] = visitOrder
      print(index+1, end = " ")
      found = 1
      break;

  if visitOrder == n: #done
    break
  elif found == 1: #not done but checked
    continue
  
  #nowhere to go
  index = dfsVisit.index(visitOrder-1)
  #index = have to find the index that has a value of visitOrder



#bfs
bfsVisit = [0 for x in range(n)]
visitOrder = 1
bfsVisit[v-1] = visitOrder
print(v, end = " ")
index = v-1

while(1):
  for i in range(n):
    if bfsVisit[i] == 0 and graph[index][i] == 1:
      visitOrder += 1
      dfsVisit[i] = visitOrder
      # print(index+1, end = " ")
