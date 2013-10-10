import sys


lines = open(sys.argv[1]).readlines()
names = lines[0].split(",")
names = sorted(names)
total = 0
nameidx = 1
for name in names:
  name = name.strip("\"")
  namescore = sum([ord(x) - ord('A') + 1 for x in name])
  if name == "COLIN":
    print nameidx
    print namescore
    print namescore * nameidx
  total = total + namescore * nameidx
  nameidx += 1

print total
  
  

