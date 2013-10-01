def sum_squares(vRange):
  return sum([v*v for v in vRange])

def square_sums(vRange):
  ans = sum(vRange)
  return ans*ans

def sum_squares_difference(vRange):
  return square_sums(vRange) - sum_squares(vRange)

print sum_squares_difference(xrange(1,101))
