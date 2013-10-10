def factorial(n):
  if n == 0:
    return 1
  return n*factorial(n-1)

def factorialsum(n):
  s = str(factorial(n))
  return sum([int(x) for x in s])

print factorialsum(100)
