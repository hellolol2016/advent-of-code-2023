f = open("xday6input.txt")
lines = "".join(f.readlines())

times = lines[lines.index(":")+1:lines.index("\n")].split(",")
lines= lines[lines.index("\n"):]
dist = lines[lines.index(":")+1:].split(",")

ans =1

for i in range(len(times)):
  count = 0
  for speed in range(int(times[i])):
    if(speed * (int(times[i])-speed)>int(dist[i])):
      count+=1
  ans *= count
print(ans)
