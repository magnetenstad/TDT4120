from lib.tests import test_algorithm, get_sort_problem_instances, \
    get_maximum_subarray_problem_instances, get_merge_sort_problem_instances, \
    get_bisect_problem_instances, get_counting_sort_problem_instances
from lib.bubble_sort import bubble_sort
from lib.insertion_sort import insertion_sort
from lib.find_maximum_subarray import find_maximum_subarray
from lib.merge_sort import merge_sort
from lib.bisect import bisect
from lib.quicksort import quicksort
from lib.counting_sort import counting_sort

def main():
    test_algorithm(bubble_sort, get_sort_problem_instances(), in_place=True)
    test_algorithm(insertion_sort, get_sort_problem_instances(), in_place=True)
    test_algorithm(merge_sort, \
        get_merge_sort_problem_instances(), in_place=True)
    test_algorithm(find_maximum_subarray, \
        get_maximum_subarray_problem_instances())
    test_algorithm(bisect, get_bisect_problem_instances())
    test_algorithm(quicksort, get_merge_sort_problem_instances(), in_place=True)
    test_algorithm(counting_sort, get_counting_sort_problem_instances(), \
        in_place=True, output=1)

if __name__ == '__main__':
    main()
