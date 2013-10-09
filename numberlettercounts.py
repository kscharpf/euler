NumToLetters = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", \
                11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}

DecinumToLetters = {20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}

def num_to_letters(x):
  if x < 20:
    return NumToLetters[x]
  elif x < 100:
    residue = ""
    if x % 10 > 0:
      residue = num_to_letters(x%10)
    return DecinumToLetters[x - x%10] + residue
  elif x < 1000:
    residue = ""
    if x % 100 > 0:
      residue = "and" + num_to_letters(x%100)
    return NumToLetters[x/100] + "hundred" + residue
  else:
    return "onethousand"

print sum([len(num_to_letters(x)) for x in range(1, 1001)])
    

  
