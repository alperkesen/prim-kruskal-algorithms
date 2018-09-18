#!/usr/bin/env python
# -*- coding: utf-8 -*-

from queue import PriorityQueue
from fibonacci_heap_mod import Fibonacci_heap


def prims(graph, start):
    """ Prim's algorith with binary heap """

    pq = PriorityQueue()
    explored = {start}

    selected_edges = []
    incident_edges = [(weight, start, v) for (v, weight) in graph[start]]

    list(map(pq.put, incident_edges))

    while not pq.empty():
        selected_edge = pq.get()
        selected_node = selected_edge[2]

        if selected_node in explored:
            continue

        selected_edges.append(selected_edge)

        explored.add(selected_node)

        for edge in graph[selected_node]:
            v, weight = edge[0], edge[1]

            if v not in explored:
                pq.put((weight, selected_node, v))

    return selected_edges


def prims_fh(graph, start):
    """ Prim's algorithm with fibonacci heap """

    pq = Fibonacci_heap()
    explored = {start}

    selected_edges = []
    incident_edges = [(weight, start, v) for (v, weight) in graph[start]]

    for edge in incident_edges:
        weight, start, v = edge
        pq.enqueue((start, v), weight)

    while pq.__nonzero__():
        selected_edge = pq.dequeue_min()
        value = selected_edge.get_value()
        selected_node = value[1]
        parent_node = value[0]
        selected_weight = selected_edge.m_priority

        if selected_node in explored:
            continue

        selected_edges.append((selected_weight, parent_node, selected_node))

        explored.add(selected_node)

        for edge in graph[selected_node]:
            v, weight = edge[0], edge[1]

            if v not in explored:
                pq.enqueue((selected_node, v), weight)

    return selected_edges
