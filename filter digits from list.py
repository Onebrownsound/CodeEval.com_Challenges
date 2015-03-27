def is_prime(n):
  'Return True if n is a prime number otherwise return False'
  x=[x for x in range(1,n+1) if n%x==0]
  if len(x)>2 or n==0 or n==1:
     return False
  else:
     return True




print (is_prime(1))
