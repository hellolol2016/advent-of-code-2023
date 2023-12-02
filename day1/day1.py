#numbers = {
  #1:"one",
  #2:"two",
  #3:"three",
  #4:"four",
  #5:"five",
  #6:"six",
  #7:"seven",
  #8:"eight",
  #9:"nine",
#}

nums = ["one","two","three","four",'five','six','seven','eight','nine']
def findleftdigit(line):
  left = 0
  while(left < len(line)):
    if(line[left].isdigit()):
      return (int(line[left]),left)
    left+=1
  return (-1,-1)

def findrightdigit(line):
  right = len(line)-1
  while(right >= 0):
    if(line[right].isdigit()):
      return (int(line[right]),right)
    right-=1
  return (-1,-1)
  

def findLeftString(line):
  min = 100000
  ans = -1
  for num in nums:
    if(line.find(num)!=-1 and line.find(num)<min ):
        ans = nums.index(num)+1
        min = line.find(num)
  return (ans,min)

def findRightString(line):
  max = -1
  ans = -1
  for num in nums:
    if(line.rfind(num)!=-1 and line.rfind(num)>max ):
        ans = nums.index(num)+1 
        max = line.rfind(num)
  return (ans,max)

def getLeft(line):
  ls = findLeftString(line)
  ld = findleftdigit(line)
  if(ls[1]>ld[1]):
    return ld[0]
  else:
    return ls[0]

def getRight(line):
  rs = findRightString(line)
  rd = findrightdigit(line)
  if(rs[1]<rd[1]):
    return rd[0]
  else:
    return rs[0]


def getAdd(line):
  ans = ""
  ans += str(getLeft(line))
  ans += str(getRight(line))
  return int(ans)

def getAns(fp):
  f = open(fp)
  ans = 0
  for line in f:
    print(getAdd(line))
    ans += getAdd(line)
  return ans

print(getAns("day1input.txt"))