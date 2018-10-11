# prim-kruskal-algorithms
Testing computational efficiency of Prim's algorithm and Kruskal's algorithm on dense and sparse graphs.

## Getting Started

In the beginning, go into the same folder as requirements.txt and install the requirements like in the below:

```bash
$ pip install -r requirement.txt
```

### Prim's algorithm

In order to use Prim's algorithm, first go into the src folder and import the module or the functions in the prims.py

```python
# Prim's algorithm with binary heap (prims) and fibonacci heap (prims_fh)

>>> from prim import prims, prims_fh

```

To use it on a graph, you should give graph and a starting point for the graph as parameters.

```python
# Importing an example graph from utils

>>> from utils import sample_graph
>>> edges = prims(sample_graph, 0)
>>> edges
[(5, 0, 1), (4, 1, 2), (6, 1, 6), (5, 6, 5), (8, 6, 7), (11, 5, 4), (7, 4, 8), (9, 4, 3)]

```

### Kruskal's algorithm

In src folder, import the functions of Kruskal's algorithm. It includes two functions where they only differ while sorting the edges by their weights.

```python
# Kruskal's algorithm with tim sort (kruskal_ts) and merge sort (kruskal_ms)

>>> from kruskal import kruskal_ts, kruskal_ms

```

Kruskal's algorithm takes a graph and edges of the graph as parameters. In order to get edges of the graph:

```python
>>> from graph import Graph
>>> from utils import sample_graph
>>> graph_kruskal = Graph()
>>> graph_kruskal.graph = sample_graph
>>> edges_kruskal = list(graph_kruskal.get_edges())
>>> edges_kruskal
[(5, 7, 10), (4, 8, 7), (1, 6, 6), (3, 5, 18), (3, 6, 23), (7, 8, 21), (3, 4, 9), (2, 3, 24), (6, 7, 8), (5, 8, 14), (5, 6, 5), (1, 2, 4), (4, 5, 11), (0, 1, 5), (1, 7, 16)]
```

Then just pass the parameters to the functions.

```python
>>> edges = kruskal_ts(sample_graph, edges_kruskal)
>>> edges
[(4, 1, 2), (5, 5, 6), (5, 0, 1), (6, 1, 6), (7, 4, 8), (8, 6, 7), (9, 3, 4), (11, 4, 5)]
```

