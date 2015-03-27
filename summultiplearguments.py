def sum_args(*args):
    total=0
    for item in args:
        total+=item
    print (total)
    return total
sum_args(5,10,15)
