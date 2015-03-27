from datetime import datetime, date, time,timedelta

def timedelta(file):
    with open(file) as f:
        
        for line in f:
            
            timearray=line.split(' ')
            
            
            if len(timearray)>1:
                t1=makeintodatatime(timearray[0])
                t2=makeintodatatime(timearray[1])
                if t1>t2:
                    t3=t1-t2
                    if len(str(t3))<8:
                        print('0'+str(t3))
                    else:
                        print(str(t3))
                else:
                    t3=t2-t1
                    if len(str(t3))<8:
                        print('0'+str(t3))
                    else:
                        print(str(t3))
            else:
                pass
               
            

def makeintodatatime(timearray):
        today=date.today()
        hour=timearray[0:2]
        minute=timearray[3:5]
        second=timearray[6:]
        r=time(int(hour),int(minute),int(second))
        t=datetime.combine(today,r)
        
        return t







timedelta('helloworld.txt')
