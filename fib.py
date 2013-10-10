cache = {}

# use memoization due to recursion limits
def fib(n):
  if n <= 2:
    return 1
  if n in cache:
    return cache[n]
  cache[n] = fib(n-1) + fib(n-2)
  return cache[n]

for i in range(1, 10000):
  s = str(fib(i))
  if len(s) == 1000:
    print "i = %d (%s)" % (i, s)
    break
