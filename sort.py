#!/usr/bin/python3
"sorts"
from copy import copy
from statistics import median

def move(arr, src, dest):
    if len(arr) == 0: return
    if dest < 0: return
    if src < 0: return
    if dest >= len(arr): return
    if src >= len(arr): return 
    register = arr[src]
    for i in range(src, dest, -1):
        arr[i] = arr[i-1]
    arr[dest] = register

# O(n^2)
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] > array[i]:
                move(array, i, j)
                break
    return array

# O(n^2)
def bubble_sort(array):
    if len(array) < 2: return
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                unsorted = True
                register = array[i+1]
                array[i+1] = array[i]
                array[i] = register

    return array

# O(n^2)
def selection_sort(array):
    if len(array) < 2: return
    for i in range(0, len(array)):
        mindex = i
        for j in range(i, len(array)):            
            if (array[j] < array[mindex]):
                mindex = j
        move(array, mindex, i)
    return array

# O(nlog(n)) REVIEW
def heap_sort(array):
    if len(array) < 2: return
    return array

# O(nlog(n))
# def merge_sort(array):
#     if len(array) < 2: return
#     for i in range(0, len(array)):
#         array[i] = [array[i]]
#     for 

#     return array

# O(nlog(n))
def quick_sort(array):
    if len(array) < 2: return array
    if len(array) == 2:
        if array[0] <= array[1]:
            return array
        else:
            return [ array[1], array[0] ]
    pivot = median([ array[0], array[len(array)-1], array[int(len(array) / 2)] ])
    wallindex = 0
    for i in range(0, len(array)):
        if array[i] < pivot:
            move(array, i, 0)
            wallindex += 1
    return (quick_sort(array[0:wallindex]) + quick_sort(array[wallindex:len(array)]))

def shell_sort(array):
    if len(array) < 2: return
    return array

def comb_sort(array):
    if len(array) < 2: return
    return array

def counting_sort(array):
    if len(array) < 2: return
    return array

def bucket_sort(array):
    if len(array) < 2: return
    return array

def radix_sort(array):
    if len(array) < 2: return
    return array

def intro_sort(array):
    if len(array) < 2: return
    return array

def tim_sort(array):
    if len(array) < 2: return
    return array


def main():
    unsorted = [ 353, 123, 296, 489, 889, 338, 639, 762, 57, 643 ]
    print("Insertion Sort: " + str(insertion_sort(unsorted)))
    unsorted = [ 353, 123, 296, 489, 889, 338, 639, 762, 57, 643 ]
    print("Bubble Sort: " + str(bubble_sort(unsorted)))
    unsorted = [ 353, 123, 296, 489, 889, 338, 639, 762, 57, 643 ]
    print("Selection Sort: " + str(selection_sort(unsorted)))
    unsorted = [ 353, 123, 296, 489, 889, 338, 639, 762, 57, 643 ]
    print("Quick Sort: " + str(quick_sort(unsorted)))

if __name__ == "__main__":
    main()
