#!/usr/bin/python3

import argparse
import os

base_dir = os.getcwd()
join = os.path.join


def main(filename):
    file = join(base_dir, filename)
    with open(file, 'r') as integers:
        a = [int(x) for x in integers]
    boundary = (0, len(a))
    sort_and_count(a, boundary)
    print(a)


def sort_and_count(a, boundary):
    n = boundary[1] - boundary[0]
    if n<=1:
        return
    pivot = select_pivot(a, boundary)
    a[boundary[0]], a[pivot] = a[pivot], a[boundary[0]]
    (left, right) = partition(a, boundary)
    sort_and_count(a, left)
    sort_and_count(a, right)


def partition(a, boundary):
    pivot_value = a[boundary[0]]
    i = boundary[0] + 1
    for j in range(boundary[0] + 1 , boundary[1]) :
        if a[j] < pivot_value :
            a[i], a[j] = a[j], a[i]
            i += 1
    a[boundary[0]], a[i - 1] = a[i - 1], a[boundary[0]]
    return (boundary[0], i - 1), (i, boundary[1])


def select_pivot(a, boundary):
    first_index = boundary[0]
    last_index = boundary[1] - 1
    center_index = first_index + (last_index-first_index)//2

    first_value = a[first_index]
    center_value = a[center_index]
    last_value = a[last_index]

    if first_value > last_value:
        if first_value > center_value:
            if center_value > last_value:
                return center_index
            else:
                return last_index
        else:
            return first_index
    else:
        if last_value > center_value:
            if center_value > first_value:
                return center_index
            else:
                return first_index
        else:
                return last_index


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Sort a list of integers from a file")
    parser.add_argument('--filename', default='IntegerList.txt')
    args = parser.parse_args()
    main(args.filename)