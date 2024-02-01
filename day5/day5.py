f = open("day5input.txt")
lines = "".join(f.readlines())

def listToMap(arr):
  temp ={}
  for item in arr:
    tempMap = item.split(" ")
    for i in range(int(tempMap[2])):
      temp[int(tempMap[1])+i] = int(tempMap[0])+i
  return temp

seeds = lines[lines.index(":")+2:lines.index("\n")].split(" ")


lines = lines[lines.index("\n")+2:]
toSoil = lines[lines.index(":")+2:lines.index("end")-1].split("\n")

soils = listToMap(toSoil)

lines = lines[lines.index("end")+2:]
toFert = lines[lines.index(":")+2:lines.index("end")-1].split("\n")

ferts  = listToMap(toFert)

lines = lines[lines.index("end")+2:]
toWater = lines[lines.index(":")+2:lines.index("end")-1].split("\n")

waters = listToMap(toWater)

lines = lines[lines.index("end")+2:]
toLight = lines[lines.index(":")+2:lines.index("end")-1].split("\n")

lights = listToMap(toLight)

lines = lines[lines.index("end")+2:]
toTemp = lines[lines.index(":")+2:lines.index("end")-1].split("\n")

temps = listToMap(toTemp)

lines = lines[lines.index("end")+2:]
toHum = lines[lines.index(":")+2:lines.index("end")-1].split("\n")

hums = listToMap(toHum)

lines = lines[lines.index("end")+2:]
toLoc = lines[lines.index(":")+2:lines.index("end")-1].split("\n")

locs = listToMap(toLoc)

# first find overlap from seed to soil, and fill in missing parts 
for seed in seeds:
  exists = False
  for sk,sv in soils.items():
    if sk == int(seed):
      exists = True
  if not exists:
    soils[int(seed)] = int(seed)


def fillBlanks(ogList, newList):
  for k,v in ogList.items():
    if not int(v) in newList:
      newList[int(v)] = int(v)

fillBlanks(soils,ferts)
fillBlanks(ferts,waters)
fillBlanks(waters,lights)
fillBlanks(lights,temps)
fillBlanks(temps,hums)
fillBlanks(hums,locs)


for seed in seeds:
  for soilK,soilV in soils.items():
    if(int(soilK)-int(seed)==0):
      for fertK,fertV in ferts.items():
        if(fertK == soilV):
          for waterK, waterV in waters.items():
            if(waterK == fertV):
              for lightK,lightV in lights.items():
                if(lightK == waterV):
                  for tempK, tempV in temps.items():
                    if(tempK == lightV):
                      for humK, humV in hums.items():
                        if(humK == tempV):
                          for locK,locV in locs.items():
                            if(locK == humV):
                              print(locV)
