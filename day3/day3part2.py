from collections import defaultdict
f = open("day3input.txt")
lines = f.readlines()
ans = 0


G = [[c for c in line.strip()] for line in lines]
R = len(G)
C = len(G[0])

nums = defaultdict(list)

for r in range(len(G)):
  gears = set()
  n = 0
  for c in range(len(G[r])+1):
    if c<C and G[r][c].isdigit():
      n = n * 10 + int(G[r][c])
      for dr in [-1,0,1]:
        for dc in [-1,0,1]:
          if(0<=r + dr<R and 0<=c+dc<C):
            char = G[r+dr][c+dc]
            if(char == "*"):
              gears.add((r+dr,c+dc))
    elif n > 0:
      for gear in gears:
        nums[gear].append(n)
      n = 0
      gears = set()

p2 = 0
for key,val in nums.items():
  if(len(val)==2):
    p2 += val[0] * val[1]

print(p2)