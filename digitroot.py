def digital_root(n):
    if n>=10:
      total=0
      digitstr=str(n)

      for elem in digitstr:
          total+=int(elem)
      print(total)
      digital_root(total)
    else:
        return n
digital_root(9421)
print(list([1,2,3,4,5]))

