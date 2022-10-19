from tokenize import String
from typing import List
from xmlrpc.client import boolean


def BubbleSort(seq:List) -> List:
    swapped = False
    n = len(seq)
    for i in range(n-1):
        for j in range(n-i-1):
            if seq[j] > seq[j+1]:
                swapped = True
                seq[j],seq[j+1] = seq[j+1],seq[j]
        if not swapped:
            break
    return seq

def SelectionSort(seq:List) -> List:
    pass

def InsertionSort(seq:List) -> List:
    pass
