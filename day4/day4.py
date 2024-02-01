f = open("day4input.txt")
lines = f.readlines()

ans = 0
for line in lines:
  targets = list(filter(None,line[line.index(":") + 2 : line.index("|")-1].split(" ")))
  cards = list(filter(None,line[line.index("|") + 2:].strip().split(" ")))
  count =0 
  for card in cards:
    if card in targets:
      if count == 0:
        count = 1
      else:
        count *= 2
  ans += count

print(ans)
