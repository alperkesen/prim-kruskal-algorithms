#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random

from graph import Graph


# Sample graph

sample_graph = {0: [(1, 5)],
                1: [(0, 5), (2, 4), (6, 6), (7, 16)],
                2: [(1, 4), (3, 24)],
                3: [(2, 24), (4, 9), (5, 18), (6, 23)],
                4: [(3, 9), (5, 11), (8, 7)],
                5: [(3, 18), (4, 11), (6, 5), (7, 10), (8, 14)],
                6: [(1, 6), (3, 23), (5, 5), (7, 8)],
                7: [(1, 16), (6, 8), (5, 10), (8, 21)],
                8: [(4, 7), (5, 14), (7, 21)]}


def generate_graph(num_node, num_edge, max_weight):
    max_edge = num_node * (num_node - 1) / 2

    if num_edge > max_edge:
        raise "Enter eligible number of edges"

    graph = Graph()
    graph.add_nodes(list(range(0, num_node)))

    edges = set()
    count_edges = 0

    for i in range(num_node-1):
        weight = random.randint(0, max_weight)
        edges.add((i, i+1))
        graph.add_edge(i, i+1, weight)

        count_edges += 1

    while count_edges != num_edge:
        n1 = random.randint(0, num_node - 1)
        n2 = random.randint(0, num_node - 1)
        weight = random.randint(0, max_weight)

        if n1 != n2 and (n1, n2) not in edges and (n2, n1) not in edges:
            edges.add((n1, n2))
            graph.add_edge(n1, n2, weight)

            count_edges += 1

    return graph


def calculate_duration(graph, algorithm, *args, **kwargs):
    start = time.time()
    algorithm(graph, args[0])
    end = time.time()

    duration = end - start

    return duration


def vals_to_str(array):
    m = "000000"
    k = "000"

    str_array = []

    for val in array:
        val_str = str(val)

        if val_str[-6:] == m:
            str_array.append(val_str[:-6] + 'm')
        elif val_str[-3:] == k:
            str_array.append(val_str[:-3] + 'k')
        else:
            str_array.append(val_str)

    return str_array
