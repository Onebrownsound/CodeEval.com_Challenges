def digitize(n):
    container=[]
    stringnumber=str(n)
    for item in stringnumber:
        container.append(int(item))
    print (container)
digitize(12345)
