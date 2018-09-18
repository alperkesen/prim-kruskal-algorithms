#!/usr/bin/env python
# -*- coding: utf-8 -*-


def merge(array, p, q, r, key=lambda t: t):
    n1 = q - p + 1
    n2 = r - q

    l_array = []
    r_array = []

    for i in range(1, n1 + 1):
        l_array.append(array[p+i-1])

    for j in range(1, n2 + 1):
        r_array.append(array[q+j])

    l_array.append((0, 0, float('inf')))
    r_array.append((0, 0, float('inf')))

    i = 0
    j = 0

    for k in range(p, r+1):
        if key(l_array[i]) <= key(r_array[j]):
            array[k] = l_array[i]
            i += 1
        else:
            array[k] = r_array[j]
            j += 1

    return array


def merge_sort(array, p, r, key=lambda t: t):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(array, p, q, key=key)
        merge_sort(array, q+1, r, key=key)
        merge(array, p, q, r, key=key)

    return array
