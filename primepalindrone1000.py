import math
def create1000():
    primelist=[]
    palindromelist=[]
    x=[x for x in range(500,1001)]
   
    for item in x:
        if is_prime(item)==True:
            primelist.append(item)
    print (primelist)

    for item in primelist:
        letters=str(item)
        if letters==letters[::-1]:
            palindromelist.append(int(letters))
    print (max(palindromelist))
    return max(palindromelist)        



def is_prime(n):
  'Return True if n is a prime number otherwise return False'
  x=[x for x in range(1,n+1) if n%x==0]
  if len(x)>2 or n==0 or n==1:
     return False
  else:
     return True
   

create1000()
