def reciprocal(numerator, d, cycles, cache):
  if numerator in cache:
    return (True, cycles - cache[numerator])
  if d > numerator:
    return reciprocal(numerator*10, d, cycles+1, cache)
  else:
    if numerator % d == 0:
      return (False, 0)
    else:
      cache[numerator] = cycles
      return reciprocal( (numerator % d) * 10, d, cycles+1, cache)

maxc = 0
maxr = 0
for i in xrange (1, 1000):
  hasCycle, period = reciprocal(1, i, 0, {})
  if hasCycle:
    if period > maxc:
      maxc = period
      maxr = i

print "Max reciprocal num: %d period %d" % (maxr, maxc)
