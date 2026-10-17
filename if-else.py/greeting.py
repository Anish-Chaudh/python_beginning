import time 
timesamp=time.strftime('%H:%M:%S')
print(timesamp)
timesmp=time.strftime(('%H'))
print(timesmp)
if("timesmp=5 and timesmp<12"):
    print("good morning everyone")
elif("timesmp=12 and timesmp<4"):
    print("good afternoon everyone")
elif("timesmp=4 and timesmp<7"):
    print("good evening everyone")
else:
    print("good night everyone")
    
