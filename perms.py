import itertools

i = 0
for p in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
  i += 1
  if i == 1000000:
    print p
