f = open("xday6input.txt")
lines = "".join(f.readlines())

time = int(lines[lines.index(":")+1:lines.index("\n")])
line= lines[lines.index("\n"):]
dist = int(lines[lines.index(":")+1:])

count = 0
for speed in range(time)):
  if(speed * (time-speed)>dist):
    count+=1
print(count)
