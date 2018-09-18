#!/usr/bin/env python
# -*- coding: utf-8 -*-


from merge_sort import merge_sort
from unionfind import UnionFind


def kruskal_ts(graph, edges):
    """ Kruskal's algorithm with tim sort """

    sorted_edges = sorted(edges, key=lambda t: t[2])
    num_nodes = len([v for v in graph])
    data_st = UnionFind(num_nodes)

    tree_edges = list()

    for edge in sorted_edges:
        (u, v, weight) = edge[0], edge[1], edge[2]

        if not data_st.find(u, v):
            tree_edges.append((weight, u, v))
            data_st.union(u, v)

        if len(tree_edges) == (num_nodes - 1):
            break

    return tree_edges


def kruskal_ms(graph, edges):
    """ Kruskal's algorithm with merge sort"""

    sorted_edges = merge_sort(edges, 0, len(edges)-1, key=lambda t: t[2])
    num_nodes = len([v for v in graph])
    data_st = UnionFind(num_nodes)

    tree_edges = list()

    for edge in sorted_edges:
        (u, v, weight) = edge[0], edge[1], edge[2]

        if not data_st.find(u, v):
            tree_edges.append((weight, u, v))
            data_st.union(u, v)

        if len(tree_edges) == (num_nodes - 1):
            break

    return tree_edges
