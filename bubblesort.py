# author:           Marcin Cherek
# python version:   2.7.11
# Date:             12th of April 2016
# language:         English
# Title:            Heapsort Algorithm python implementation

#public <bubbleSort>
#We iterate the Elements and compare them
#to each other. If the Element is bigger than
#it will be compared with the next one. Until it is
#smaller or it is the biggest Element
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
