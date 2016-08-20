# author:           Marcin Cherek
# python version:   2.7.11
# Date:             12th of April 2016
# language:         English
import logging
import heapsort
import mergesort
import quicksort
import bubblesort
import radixsort

logging.basicConfig()
logger= logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

# These are the sorttypes you can choose in this package.
sort_types = enum("heapsort","mergesort", "quicksort","bubblesort","radixsort")

#For the Exception
FALSE_TYPE = str("Only Lists suported")

# This prepares the data to sort.
# We dont ned for example a whole list with dictionaries.
# We need just the numbers to sort.
def __prepareList(aList,key):
    result = []
    for i in range(0, len(aList),+1):
        result.append(aList[i]["".join(key)])
    return result

# This prepare the result. We just sorted the part we had to.
# But now we will give back the whole data so we map them together.
def __prepareResult(result,origin,key):
    preparedResult = []
    for i in range(0,len(result),+1):
        for n in range(0,len(result),+1):
            if(int(result[i])==int(origin[n]["".join(key)])):
                preparedResult.append(origin[n])
    return preparedResult
    
# Most important method.
def sort(aList, sort_typ ,*key):
    if( isinstance(aList,list)==False):
        raise TypeError(FALSE_TYPE)
    if(len(aList)<=1):
        return aList
    logger.info("Input Size:" +str(len(aList)-1))
    origin = aList
    if(key is not ()):aList = __prepareList(aList,key)
    result = []
    if(sort_typ == sort_types.heapsort):
        result = heapsort.heapsort(aList)
    elif(sort_typ == sort_types.mergesort):
        result = mergesort.merge_sort(aList)
    elif(sort_typ == sort_types.quicksort):
        result = quicksort.quicksort(aList)
    elif(sort_typ == sort_types.bubblesort):
        result = bubblesort.bubbleSort(aList)
    elif(sort_typ == sort_types.radixsort):
    	result = radixsort.radixsort(aList)
    if(key is not ()):result = __prepareResult(result,origin,key)
    logger.info("Input Size:" +str(len(result)-1))
    return result
        
