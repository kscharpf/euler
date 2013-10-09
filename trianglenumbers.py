import math
def next_triangle_number(index, prev_sum):
  return prev_sum + index

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
  factors.append(num)
  return factors

done = False
idx = 1
n = 0 
max_x = 0
while not done:
  n = next_triangle_number(idx, n)
  x = len(divisors(n))
  if x > 500:
    print "Answer: %d" % n
    done = True
  idx += 1
  if idx % 1000 == 0:
    print idx, n, max_x
  if x > max_x:
    max_x = x
  
