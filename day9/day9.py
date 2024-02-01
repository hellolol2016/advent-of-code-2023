f = open("day9input.txt")
lines = f.readlines()

p1 = 0

def findValue(nums):
  prev = int(nums[0])
  dif = int(nums[1])-int(nums[0])
  numind = 0
  samedif = True  
  for num in nums[1:]:

    if not int(num)-prev == dif:
      samedif = False

    dif = int(num) - prev
    nums[numind] = dif
    numind+=1
    prev = int(num)

  if (samedif):
    return dif + int(nums[-1])
  return int(nums[-1]) + findValue(nums[:-1])  


for line in lines:
  nums = line.strip().split(" ")
  nums = nums[::-1]
  p1 += findValue(nums)

print(p1)