import timeit
import random
import matplotlib.pyplot as plt


def insertion_sort(array_):
    # Got this implementation of insertion sort from this link:
    # https://www.geeksforgeeks.org/python-program-for-insertion-sort/
    for i in range(1, len(array_)):
        key = array_[i]
        j = i - 1
        while j >= 0 and key < array_[j]:
            array_[j + 1] = array_[j]
            j -= 1
        array_[j + 1] = key


def merge_sort(array_):
    # Got this implementation of merge sort from this link:
    # https://how.dev/answers/merge-sort-in-python
    if len(array_) > 1:
        mid = len(array_) // 2
        left_half = array_[:mid]
        right_half = array_[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array_[k] = left_half[i]
                i += 1
            else:
                array_[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array_[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array_[k] = right_half[j]
            j += 1
            k += 1


def time(sort_function, arr):
    return timeit.timeit(lambda: sort_function(arr.copy()), number=1)


def test():
    sizes = [10, 50, 100, 500, 1000, 5000, 10000, 20000]
    insertion_times = {'random': [], 'sorted ascending': [], 'sorted descending': []}
    merge_times = {'random': [], 'sorted ascending': [], 'sorted descending': []}

    for size in sizes:
        data_random = random.choices(range(10001), k=size)
        data_sorted_ascending = list(range(size))
        data_sorted_descending = list(range(size, 0, -1))
        list_of_data = [data_random, data_sorted_ascending, data_sorted_descending]

        for data, label in zip(list_of_data, insertion_times.keys()):
            insertion_times[label].append(time(insertion_sort, data))
            merge_times[label].append(time(merge_sort, data))

    plt.figure(figsize=(10, 6))
    plt.xlabel("Input size")
    plt.ylabel("Time (seconds)")
    plt.title("Insertion Sort vs Merge Sort")

    for label in insertion_times.keys():
        plt.plot(sizes, insertion_times[label], marker='o', linestyle='--', label=f'Insertion Sort ({label})')
        plt.plot(sizes, merge_times[label], marker='s', linestyle='-', label=f'Merge Sort ({label})')

    plt.legend()
    plt.yscale('log')
    plt.grid(True)
    plt.savefig("graph_insertion_sort_vs_merge_sort.png")


if __name__ == "__main__":
    test()