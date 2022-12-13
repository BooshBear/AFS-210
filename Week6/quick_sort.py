import time
import random

def quick_sort(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partitionStart(a_list, start, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
    


def partitionStart(a_list, start, end):
    return partition(a_list, start, end)

def partition(a_list, start, end):
    # Select the first element as our pivot point
    pivot = a_list[start]
    
    # Start at the first element past the pivot point
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and a_list[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and a_list[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            # Swap the values
            a_list[low], a_list[high] = a_list[high], a_list[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    # Swap the values
    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high


print("Quick Sort:")
#myList = [54,26,93,17,77,31]
myList = [x for x in range(1000)]
random.shuffle(myList)

#print(myList)
start_time = time.time()
quick_sort(myList,0,len(myList)-1)
end_time = time.time()
#print()
#print("Sorted Listed: ")
#print(myList)   

print(f"The first execution time is: {end_time-start_time}")

# -- My Code --

# This one is random start where it starts from a random place in the list
def quick_sort2(a_list, start, end):
    if start >= end:
        return

    pivot = partitionStart(a_list, random.randrange(0, len(a_list)), end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)

myList2 = [x for x in range(1000)]
random.shuffle(myList2)

print("Quick Sort:")
#myList2 = [54,26,93,17,77,31]
start_time2 = time.time()
quick_sort2(myList2,0,len(myList2)-1)
end_time2 = time.time()

print(f"The second execution time is: {end_time2-start_time2}")

# This will be it starting at the end of the list instead of the start
def quick_sort3(a_list, start, end):
    if start >= end:
        return

    pivot = partitionStart(a_list, end, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)

myList3 = [x for x in range(1000)]
random.shuffle(myList3)

print("Quick Sort:")
#myList2 = [54,26,93,17,77,31]
start_time3 = time.time()
quick_sort3(myList3,0,len(myList3)-1)
end_time3 = time.time()

print(f"The third execution time is: {end_time3-start_time3}")

# This time it will start at absolute medium
def quick_sort4(a_list, start, end):
    if start >= end:
        return
    medium = sum(a_list)//len(a_list)
    pivot = partitionStart(a_list, medium, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)

# myList4 = [54,26,93,17,77,31]
myList4 = [x for x in range(1000)]
random.shuffle(myList4)


print("Quick Sort:")
# print(myList4)
start_time4 = time.time()
quick_sort3(myList4,0,len(myList4)-1)
end_time4 = time.time()
# print(myList4)

print(f"The fourth execution time is: {end_time4-start_time4}")