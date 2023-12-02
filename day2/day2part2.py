f = open("day2input.txt")
lines = f.readlines()
ans = 0
for line in lines: 
  nextline = True
  line = line[line.index(":")+2:]

  colors = {
    "red":0,
    "green":0,
    "blue":0,
  }
  for bag in line.split("; "):
    for color in bag.split(", "):
      num = int(color[:color.index(" ")])
      stringColor = color[color.index(" ")+1:].strip()
      if(colors[stringColor] < num):
        colors[stringColor] = num
  temp = 1
  for x in colors:
    temp *= colors[x]
  print(temp)
  ans += temp
  

print(ans)