def is_prime(n):
  if n <= 0:
    return False
  d = 2
  while (n/2+1) > d:
    if n % d == 0:
      return False
    d += 1
  return True

def quadnum(n, a, b):
  return n*n+a*n+b

def consecutiveprimes(a, b):
  n = 0
  while is_prime(quadnum(n, a, b)):
    n += 1
  return n 

def evalquads():
  maxn = 0
  for a in xrange(-999, 1000):
    if a % 100 == 0:
      print "a: %d" % a
    for b in xrange(-999, 1000):
      n = consecutiveprimes(a,b)
      if n > maxn:
        maxn = n
        maxa = a 
        maxb = b
        print "maxn: %d maxa %d maxb %d prod %d" % (maxn, maxa, maxb, maxa*maxb)
 
evalquads() 
    
  
