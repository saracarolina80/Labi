
def fatorial(x):

  if not isinstance ( x , int ):
    return "invalid"
  
  
  if x < 0:
    return "invalid"
  
  if x == 0:
    return 1
  
  res = 1
  while x > 0:
    res = res * x
    x = x - 1
    
  return res

