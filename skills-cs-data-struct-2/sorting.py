#Sorting

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    # num_of_passes is the total items in the list
    # for bubble sort we need to keep iterating until the end of the list
    # as our passes (excluding the last item). Then within those num_of_passes,
    # we have to loop again, the length of the num_of_passes.
    for num_of_passes in range(len(lst)-1, 0, -1):
        for i in range(num_of_passes):
            if lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    list_c = []
    # first check the 0th element of list1, list2
    # compare their values
    # put them in list c
    while len(list1) > 0 or len(list2) > 0:
        if list1 == []:
            list_c.append(list2.pop(0))
        elif list2 == []:
            list_c.append(list1.pop(0))
        elif list1[0] < list2[0]:
            list_c.append(list1.pop(0))
        else:
            list_c.append(list2.pop(0))
    print list_c


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    if len(list1) == 1:
        return list1
    if len(list2) == 1:
        return list2
    list_div_value = len(lst)/2
    list1 = lst[:list_div_value]
    list2 = lst[list_div_value:]

    halved_list = merge_lists(list1, list2)

    # idea: the recursive step is actually the divide the list into smaller
    # segments step. We will continue to divide the list until one of the lists
    # have only one element in it.

# Yeah, I don't know the solution, but here is a close enough version:
# def divide_stuff(listy):
#     new_list = []
#     divided_val = len(listy)/2
#     bloop = listy[divided_val:]

#     if len(listy) == 1:
#         return listy
#     else:
#         blah = divide_stuff(listy[:divided_val])
#     sorted_list = merge_lists(blah, bloop)
#     return sorted_list
# divide_stuff([6, 2, 3, 9, 0, 1])


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print