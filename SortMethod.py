from typing import List

# Bubble Sort 冒泡排序 Best: O(N) Worst: O(N2) 稳定
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

# Selection Sort 选择排序 Every situations: O(N2) 不稳定
def SelectionSort(seq:List) -> List:
    n = len(seq)
    for i in range(n-1):
        curr_index = i
        for j in range(i+1,n):
            if seq[j] < seq[curr_index]:
                curr_index = j
        seq[i],seq[curr_index] = seq[curr_index],seq[i]
    return seq

# Insertion Sort 插入排序 Best: O(N) Worst: O(N2) 稳定
def InsertionSort(seq:List) -> List:
    n = len(seq)
    for i in range(1,n):
        curr = seq[i]
        j = i - 1
        while j >= 0 and seq[j] > curr:
            seq[j+1] = seq[j]
            j -= 1
        seq[j+1] = curr
    return seq

#  Merge Sort 归并排序 Every situation O(nlogn) 稳定
def MergeSort(seq:List) -> List:
    if len(seq) < 2: return seq
    left = MergeSort(seq[:len(seq)//2])
    right = MergeSort(seq[len(seq)//2:])
    return Merge(left,right)

def Merge(left:List,right:List) -> List:
    res,i,j = [],0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

# Quick sort 快速排序
def QuickSort(seq:List) -> List:
    pass