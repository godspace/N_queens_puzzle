def check(map, x, y):
  #check line
  i = 0
  j = y
  while i < N:
    if map[j][i] == 1:
      return False
    i += 1
  #check upper left diagonal
  i = x
  j = y
  while i >= 0 and j >= 0:
    if map[j][i] == 1:
      return False
    i -= 1
    j -= 1
  #check bottom left diagonal
  i = x
  j = y
  while i >= 0 and j < N:
    if map[j][i] == 1:
      return False
    i -= 1
    j += 1
  #if all checks passed
  return True
#generate board(map)
def board(x, y):
  map = []
  while y < N:
    map.append([])
    while x < N:
      map[y].append(0)
      x += 1
    x = 0
    y += 1
  return (map)

N = 5 #board scale
sum_answ = 0 #answers counter
map = board(0, 0) #generate new board to arr map

#Solver
def put_Queen(map, x, y):
  global sum_answ
  if x >= N: #condition for stopping recursion
      print (map)
      sum_answ += 1
      print (sum_answ)
      return True
  while y < N: #pass through all rows from 0 to N. And also through all collomns(recursively)
    if check(map, x, y): #if possible to put Queen
      map[y][x] = 1 #put it
      put_Queen(map, x + 1, 0) #recursively call this function again
      map[y][x] = 0 #if can't put queen - delete previous one
    y += 1
  return sum_answ
print (put_Queen(map, 0, 0))
