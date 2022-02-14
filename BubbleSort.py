import random
import time

start = time.time()
isAligned = True

def BubbleSort(a):
    
    n = len(a)
    
    while n > 0:
        lastTrade = 0
        for i in range(n-1):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                lastTrade = i
        n = lastTrade
        
    return a

def CreateRandomList():
    numList = []
    for i in range(1, 5001):
        number = random.randint(1, 5001)
        numList.append(number)
    #f = open("새파일.txt", 'w')
    #f.write(str(numList))
    #f.close()
    return numList;

def Main():
    data = CreateRandomList()
    
    #f = open("새파일.txt", 'r')
    #data = f.read().split(', ')
    #f.close()
    
    print("데이터 처리 시작")
    
    #print("정렬 전 자료")
    #print (data)
    
    BubbleSort(data)
    
    #print("정렬 후 자료")
    #print (data)

Main()

print("time :", time.time() - start)