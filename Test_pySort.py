# author:           Marcin Cherek
# python version:   2.7.11
# Date:             12th of April 2016
# language:         English
# TEST CASES for pySortLite

import pySort
import unittest

# We Test our three Algorithms with the same cases
# Case 1:Normal List to sort
# Case 2:Nothing to sort
# Case 3:List of dictionaries to sort //with key
class pySortTest(unittest.TestCase):

    def testHeapSort(self):
        self.assertEquals(pySort.sort([1,2,3,4],pySort.sort_types.heapsort),[4,3,2,1])
        self.assertEquals(pySort.sort([],pySort.sort_types.heapsort),[])
        self.assertEquals(pySort.sort([{"likes":20},{"likes":40}],pySort.sort_types.heapsort,"likes"),[{"likes":40},{"likes":20}])

    def testMergeSort(self):
        self.assertEquals(pySort.sort([1,2,3,4],pySort.sort_types.mergesort),[4,3,2,1])
        self.assertEquals(pySort.sort([],pySort.sort_types.mergesort),[])
        self.assertEquals(pySort.sort([{"likes":20},{"likes":40}],pySort.sort_types.mergesort,"likes"),[{"likes":40},{"likes":20}])

    def testQuickSort(self):
        self.assertEquals(pySort.sort([1,2,3,4],pySort.sort_types.quicksort),[4,3,2,1])
        self.assertEquals(pySort.sort([],pySort.sort_types.quicksort),[])
        self.assertEquals(pySort.sort([{"likes":20},{"likes":40}],pySort.sort_types.quicksort,"likes"),[{"likes":40},{"likes":20}])

    def testBubbleSort(self):
        self.assertEquals(pySort.sort([1,2,3,4],pySort.sort_types.bubblesort),[4,3,2,1])
        self.assertEquals(pySort.sort([],pySort.sort_types.bubblesort),[])
        self.assertEquals(pySort.sort([{"likes":20},{"likes":40}],pySort.sort_types.bubblesort,"likes"),[{"likes":40},{"likes":20}])


if __name__ == "__main__":
    unittest.main()
