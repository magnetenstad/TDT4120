from lib.tests import get_bucket_sort_problem_instances, test_algorithm, get_sort_problem_instances, \
    get_maximum_subarray_problem_instances, get_merge_sort_problem_instances, \
    get_bisect_problem_instances, get_counting_sort_problem_instances, \
    get_radix_sort_problem_instances, get_randomized_select_problem_instances, \
    get_heapsort_problem_instances
from lib.bubble_sort import bubble_sort
from lib.insertion_sort import insertion_sort
from lib.find_maximum_subarray import find_maximum_subarray
from lib.merge_sort import merge_sort
from lib.bisect import bisect
from lib.quicksort import quicksort
from lib.counting_sort import counting_sort
from lib.radix_sort import radix_sort
from lib.bucket_sort import bucket_sort
from lib.randomized_select import randomized_select
from lib.heapsort import heapsort


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
    test_algorithm(radix_sort, get_radix_sort_problem_instances())
    test_algorithm(bucket_sort, get_bucket_sort_problem_instances())
    test_algorithm(randomized_select, get_randomized_select_problem_instances())
    test_algorithm(heapsort, get_heapsort_problem_instances(), in_place=True)


if __name__ == '__main__':
    main()
