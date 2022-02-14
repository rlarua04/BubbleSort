import random
import time

start = time.time()

def BubbleSort(a):
    
    n = len(a)
    
    for i in range(n):
        for j in range(1, n - i):
            if a[j - 1] > a[j]:
                temp = a[j - 1]
                a[j - 1] = a[j]
                a[j] = temp    
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
    #data = f.read().split(',')
    #f.close()

    print("데이터 처리 시작")

    #print("정렬 전 자료")
    #print (data)
    
    BubbleSort(data)
    
    print("정렬 후 자료")
    print (data)

Main()

print("time :", time.time() - start)