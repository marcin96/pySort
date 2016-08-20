# author:           Marcin Cherek
# python version:   2.7.11
# Date:             12th of April 2016
# language:         English
# Title:            Heapsort Algorithm python implementation

def heapsort(aList):
    return __heapsort(aList)

# PUBLIC: <<HeapSort>>
# We build a heap with the rules
# To build a heap we start a the index of the leastparent
# and iterate to the root Element index of 0. step -1
# In the Second step we flat the Heap to an Array. We start at the 
# last nodes Index and and Iterate to zero with step -1.
# In each repeat we swap the root Element with the last Element and 
# rebuild our Heap with the rules. This leads to an shrinking Heap.
# The last repeat is when we have a Heap with only 2 Nodes.
def __heapsort(aList):
    # List to Heap
    length = len(aList) - 1
    #We start at the index with the least parent because our down method need childnodes.
    for i in range(abs(length / 2), -1, -1):
        __down(aList, i, length)
    # Heap to List
    for i in range(length, 0, -1):
        #swaps the last element with the rootElement
        __swap(aList, 0, i)
        #restore Heap rules for our smaller getting heap
        __down(aList, 0, i - 1)
    return aList


# PRIVATE: <<Down>>
# First we calculate the Children. Left = 2n and Right = 2n+1
# Then we look if the children exists and if they are bigger than
# the parent we swap the elements.
def __down(aList, current, heapSize):
    leftC = 2 * current
    rightC = leftC + 1
    if (leftC <= heapSize and rightC > heapSize):
        #Just one Child on the left site
        if (aList[leftC] < aList[current]):
            __swap(aList, leftC, current)
    else:
        if (rightC <= heapSize):
            #There are two children and it's possible that they are also
            #Parent's
            child = 0
            if (aList[leftC] < aList[rightC]):
                child = leftC
            else:
                child = rightC
            if (aList[child] < aList[current]):
                __swap(aList, current, child)
                __down(aList, child, heapSize)

#PRIVATE: <<SWAP>>
# Swap means to exchange a node with his child
# idx_one and idx_two are the indexes
def __swap(aList, idx_one, idx_two):
    #logger.info(("SWAP:", aList[idx_one], aList[idx_two]))
    tmp = aList[idx_one]
    aList[idx_one] = aList[idx_two]
    aList[idx_two] = tmp


if __name__ == "__main__":
    print("RESULT:"+str(heapsort([2, 3, 21, 56, 53, 2, 1, 6, 2, 3, 2, 4, 5, 6, 5, 5, 3, 3, 4, 100])))
