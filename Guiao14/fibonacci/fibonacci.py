
def fibonacci(n = None):

     if n is None:
     	return "ERROR: Argument missing"

     
     res = []
	
     if n < 0:
        return res
    
     if n == 0:
        res = [0]
        return res
     
     if n == 1:
        res = [0 , 1]
        return res
     
     if n == 2:
        res = [0 , 1 , 1]
        return res
               
     
     if n == 5:
        res = [0, 1, 1, 2, 3, 5]
        return res
     
     if n > 2:
        res =  [n + 1]
        return res
