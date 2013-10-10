import math

def divisors(num):
  i = 2
  factors = []
  while i < math.sqrt(num):
    if num%i == 0:
      factors.append(i)
      factors.append(num/i)
    i += 1
  if i*i == num:
    factors.append(i)
  factors.append(1)
  return factors

def is_abundant(n):
  f = divisors(n)
  if sum(f) > n:
    return True
  return False

abundantnums = []
for i in range(12, 28124):
  if is_abundant(i):
    abundantnums.append(i)

def is_abundant_sum(n):
  global abundantnums
  j = 0
  sumfound = False
  while j < len(abundantnums) and sumfound == False:
    if abundantnums[j] > n:
      return False
    k = j
    while k < len(abundantnums) and sumfound == False:
      if abundantnums[j] + abundantnums[k] > n:
        break
      if abundantnums[j] + abundantnums[k] == n:
        return True
      k += 1
    j += 1
  return False

total = 0
for i in xrange(1,28124):
  if i % 100 == 0:
    print "i = %d" % i
  if not is_abundant_sum(i):
    total += i

print total


  
   
#print is_abundant_sum(24, abundantnums)
#print sum(nosum)
#print is_abundant(13)
    
