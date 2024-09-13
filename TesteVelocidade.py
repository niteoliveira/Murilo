import time
#1)
problemSize = 5000
print("%12s%16s" %("Problem Size","Seconds"))
for count in range(5):
    start = time.time( )
    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1
    elapsed = time.time() - start
    print("%12d%16.5f" %(problemSize,elapsed))
    problemSize *= 4
#2)


problemSize = 1000
print("%12s%16s" %("Problem Size","Interations"))
for count in range(5):
    number = 0
    work = 1
    for x in range(problemSize):
        for k in range(problemSize):
            number +=1 
            work += 1
            work -= 1
    
    print("%12d%16.5f" %(problemSize,number))
    problemSize *= 2
