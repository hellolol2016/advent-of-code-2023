f = open("day2input.txt")
lines = f.readlines()
ans = 0
game = 1
for line in lines: 
  nextline = True
  line = line[line.index(":")+2:]
  for bag in line.split("; "):
    if(not nextline): break
    for color in bag.split(", "):
      num = int(color[:color.index(" ")])
      stringColor = color[color.index(" ")+1:]
      if((stringColor == "blue" and num > 14) or (stringColor == "red" and num > 12) or (stringColor == "green" and num >13) ):
        nextline = False 
        break
  if( nextline):ans +=  game
  else:print(""+str(game) + " is bad")
  game+=1
  

print(ans)