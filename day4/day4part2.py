f = open("day4input.txt")
lines = f.readlines()

instances = [1] * 200

ans = 0
for i in range(len(lines)):
  targets = list(filter(None,lines[i][lines[i].index(":") + 2 : lines[i].index("|")-1].split(" ")))
  cards = list(filter(None,lines[i][lines[i].index("|") + 2:].strip().split(" ")))
  matches =0 
  for card in cards:
    if card in targets:
      matches += 1

  for j in range(matches):
    if(i+j+1 < 200):
      instances[i+j+1]+=instances[i]



for i in instances:
  ans += i

print(instances)
print(ans)
