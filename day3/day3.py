f = open("day3input.txt")
lines = f.readlines()
ans = 0
def checkRow(arr):
  for item in arr:
    if(not item.isdigit() and not item == "."):
      return True
  return False
def checkCol(item):
  return not item.isdigit() and not item =="."


for row in range(len(lines)): 
  col = 0
  while col < len(lines[0])-2:
    if(lines[row][col].isdigit()):
      numlen = 1
      while(lines[row][col+numlen].isdigit()):
        numlen += 1
      top = False
      left = False
      bot = False
      right = False
      if(row > 0):
        leftInd = max(0,col-1)
        rightInd = min(col+numlen+1,139)
        top = checkRow(lines[row-1][leftInd:rightInd])
      if(col > 0):
        left = checkCol(lines[row][col-1])
      if(row < len(lines)-1):
        leftInd = max(0,col-1)
        rightInd = min(col+numlen+1,139)
        bot = checkRow(lines[row+1][leftInd:rightInd])
      if(col+numlen < len(lines[0])-1):
        right = checkCol(lines[row][col+numlen])

      if(int(lines[row][col:col+numlen]) == 46):
        print(""+str(top) + str(bot) )
        print(str(left) + str(right))
        print(lines[row][col+numlen])

      if(top or bot or left or right):
        print(lines[row][col:col+numlen])
        ans += int(lines[row][col:col+numlen])
      
      col = col+numlen
    col+=1
print(ans)