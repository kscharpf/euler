

def find_triplet(maxV):
  for a in range(1,maxV):
    for b in range(1,maxV):
      if a+b >= maxV:
        continue
      for c in range(maxV):
        if a+b+c == maxV:
          if a*a + b*b == c*c:
            return a, b, c

a,b,c = find_triplet(1000)
print a*b*c
