 
def diagcount(dim):
  diff = 0
  delta = 2
  lastd = (1,1,1,1)
  total = 1
  for i in range(dim/2):
    nextbr = lastd[0] + delta
    nextbl = lastd[1] + delta + 2
    nextul = lastd[2] + delta + 4
    nextur = lastd[3] + delta + 6
    lastd = (nextbr, nextbl, nextul, nextur)
    delta += 8
    total += sum(lastd)
    
  return total

print diagcount(1001)

