import random
import time

start = time.time()
isAligned = True

def BubbleSort(a):
    
    n = len(a)
    
    for i in range(n - 1):
        isAligned = True
        for j in range(1, n - i):
            if a[j - 1] > a[j]:
                isAligned = trade(a, j)
            
        if isAligned == True:
            print(i-1, "번째 완료됨")
            break
                 
    return a

def trade(a, j):
    temp = a[j - 1]
    a[j - 1] = a[j]
    a[j] = temp
    return False;

def CreateRandomList():
    numList = []
    for i in range(1, 2000):
        number = random.randint(1, 2001)
        numList.append(number)
    f = open("새파일.txt", 'w')
    f.write(str(numList))
    f.close()
    return numList;

def Main():
    #data = CreateRandomList()
    
    f = open("새파일.txt", 'r')
    data = list(f.readline())
    f.close()
    
    print("데이터 처리 시작")
    
    #print("정렬 전 자료")
    #print (data)
    
    BubbleSort(data)
    
    #print("정렬 후 자료")
    #print (data)

Main()

print("time :", time.time() - start)