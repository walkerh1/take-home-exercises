# q1 Veyor take-home.

# Note: it is more pythonic to replace the custom comparator and
# cmp_to_key below with the following line:

    # array.sort(key=lambda x: (frequencies[x], x))

# This line works because python tuples have an order defined on them:
# given two tuples, python first compares the elements in position 0,
# and if they're equal, it then compares the elements in position 1,
# and so on. The reason I went with a custom_comparator instead is 
# because it shows more explicitly the logic of the sorting algorithm,
# and looks less like I just googled how to sort an array by frequency.


from collections import defaultdict
from functools import cmp_to_key


def custom_sort(array):
    """
    Implements custom sort algorithm.
    """
    # Get frequency of each number in array - O(n) time
    frequencies = defaultdict(int)
    for number in array:
        frequencies[number] += 1
    
    # This function helps the sorting function swap an element with the
    # element to its right if it has a higher frequency; and if it has
    # the same frequency, swap it only if it has a greater value.
    def custom_comparator(num1, num2):
        freq1 = frequencies[num1]
        freq2 = frequencies[num2]
        if (freq1 == freq2):
            return num1 - num2
        return freq1 - freq2
    
    # Creates and returns sorted version of array in O(nlogn) time.
    return sorted(array, key=cmp_to_key(custom_comparator))


def custom_sort_and_print(array):
    """
    Calls custom_sort on given array and prints results.
    """
    sorted_list = custom_sort(array)
    print('')
    for number in sorted_list:
        print(number)


if __name__ == '__main__':
    try:
        n = int(input())
        array = []
        i = 0
        while i < n:
            next_number = int(input())
            array.append(next_number)
            i += 1
        custom_sort_and_print(array)
    except ValueError:
        print('Please input integers only.')
        exit(1)
