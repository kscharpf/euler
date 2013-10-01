def is_multiple(n, x):
  return n % x == 0

def is_multiple_range(n, minV, maxV):
  return all(is_multiple(n, v) for v in xrange(minV, maxV+1))

startV = 2520
val = startV
while not is_multiple_range(val, 1, 20):
  val += 2520 

print "Answer: " + str(val)
