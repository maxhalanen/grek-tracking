import math

class Solution:
  def findPermutation(self, str1, pattern):

    check = {}
    start = 0

    if len(pattern) > len(str1):
      return False

    for i in range(len(pattern)):
      char = pattern[i]
      if char not in check:
        check[char] = 0
      check[char] += 1
    
    matched = 0
    for end in range(len(str1)):
      char = str1[end]

      if char in check:
        check[char] -= 1
        if check[char] == 0:
          matched += 1
      
      if matched == len(check):
        return True

      if end >= len(pattern) - 1:
        
        if str1[start] in check:
          if check[str1[start]] == 0:
            matched -= 1
          check[str1[start]] += 1

        start += 1

    return False
