from random import randint
import sys
sys.setrecursionlimit(10000)

def sortcheck():
    global isSorted
    sortCount = 0
    for i in range(len(arr)):
        if i + 1 < len(arr):
            if arr[i] <= arr[i + 1]:
                sortCount += 1
    if sortCount + 1 == len(arr):
        isSorted = True
        print("-----Dataset is sorted!--------")
    else:
        isSorted = False
        print("is sorted false")
        randomise()


def randomise():
    samenumber = []
    arrPH = []
    global arr
    while len(samenumber) < len(arr):
        value = randint(0, (len(arr) - 1))

        if value not in samenumber:
            samenumber.append(value)
            arrPH.append(arr[value])
    arr = arrPH
    print(arr)
    sortcheck()

arr = [1, 3, 2, 55,22,12,999,858]
sortcheck()
