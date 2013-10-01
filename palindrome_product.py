def is_palindrome(x):
  s = str(x)
  if s[:len(s)/2] == s[len(s)/2:][::-1]:
    return True
  return False

def is_palindrome_product(x,y):
  return is_palindrome(x*y)

palindromes = []
for x in range(100, 1000):
  for y in range(100, 1000):
    if is_palindrome_product(x,y):
      palindromes.append(x*y)
print max(palindromes)
