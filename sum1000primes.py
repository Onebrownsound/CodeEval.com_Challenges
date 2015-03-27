def create1000():
    primelist=[]
    x=[x for x in xrange(1,7920)]
   
    for item in x:
        if is_prime(item)==True:
            primelist.append(item)
    print (sum(primelist))

def is_prime(n):
  'Return True if n is a prime number otherwise return False'
  x=[x for x in xrange(1,n+1) if n%x==0]
  if len(x)>2 or n==0 or n==1:
     return False
  else:
     return True
   

create1000()

