# author:           Marcin Cherek
# python version:   2.7.11
# Date:             12th of April 2016
# language:         English
# Title:            Mergesort Algorithm python implementation


# divide conquer combine
# First we split te List and then we sort the parts.
# At the end we combine the parts together to one Solution
# We split until it is not more possible to split. Then we compare
# the splited parts.
# We return all sorted Parts combined in one List
def merge_sort(aList):
    middle = len(aList) /2
    leftPart = aList[:middle]
    rightPart = aList[middle:]
    if(middle >0):
        leftPart = merge_sort(leftPart)
        rightPart = merge_sort(rightPart)
    return list(__merge(leftPart,rightPart))


def __merge(leftPart,rightPart):
    sortedL = []
    left_index, right_index = 0,0
    while left_index < len(leftPart) and right_index <len(rightPart):
        if( leftPart[left_index] >= rightPart[right_index]):
            sortedL.append(leftPart[left_index])
            left_index +=1
        else:
            sortedL.append(rightPart[right_index])
            right_index +=1
    if leftPart:
        sortedL.extend(leftPart[left_index:]) #Extend adds a Lists content
    if rightPart:
        sortedL.extend(rightPart[right_index:])
    return sortedL
