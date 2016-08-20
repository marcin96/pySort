# author:           Marcin Cherek
# python version:   2.7.11
# Date:             12th of April 2016
# language:         English
# Title:            Heapsort Algorithm python implementation


# divide conquer combine
# First we choose a element to compare (pivot)
# Then we put all smaller elements in a list and
# all bigger elements in a list.
# The elements that equals the pivot goes to the pivotList.
# This method is recursive so we repeat it until they are no
# more smaller or greater elements then the pivot.
# At the end we return te more + pivotList + less.
def quicksort(aList): 
    return __quickSort(aList)

def __quickSort(aList):
    less = []
    pivotList =[]
    more =  []
    if(len(aList)>0):
        pivot = aList[0]
        for i in aList:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = __quickSort(less)
        more = __quickSort(more)
    return more + pivotList + less
