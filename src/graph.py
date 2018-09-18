#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Graph:
    def __init__(self):
        self.graph = {}
        self.num_edges = 0
        self.num_nodes = 0

    def add_node(self, node):
        self.graph[node] = list()
        self.num_nodes += 1

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_edge(self, node, node2, weight):
        self.graph[node].append((node2, weight))
        self.graph[node2].append((node, weight))
        self.num_edges += 1

    def get_nodes(self):
        return [node for node in self.graph]

    def get_edges(self):
        edges = set()

        for u in self.graph:
            for (v, weight) in self.graph[u]:
                if (v, u, weight) not in edges:
                    edges.add((u, v, weight))

        return edges

    def get_graph(self):
        return self.graph

    def number_of_nodes(self):
        return self.num_nodes

    def number_of_edges(self):
        return self.num_edges



