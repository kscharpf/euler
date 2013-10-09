def power_digit_sum(x):
  s = str(x)
  return sum([int(c) for c in s])

print power_digit_sum(2**1000)
  
