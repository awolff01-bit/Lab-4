def divisible_by_m(n,m):
  """
  Return whether n is divisible by m.

  >>> divisible_by_m(3,2)
  False
  >>> divisible_by_m(0,4)
  True
  >>> divisible_by_m(-6, 2)
  True
  >>> divisible_by_m(10,5)
  True
  """
  return n % m == 0
  
  
