import streamlit as st
from functions import display as dsp, algorithms as ga

# TODO: decide what to do with eccentricity ==0 and nodes which only reach one other node (not the center of the graph!)

# TODO: implement a button for effectively stop the app instead of crashing

# TODO: calculate shortest paths and save in session state.
# TODO: rewrite diameter and average path as for the GCC.

# TODO: how to visualize distribution
# TODO: plot the distribution using the display function.

G, undirected_G = st.session_state.G, st.session_state.undirected_G

st.write(r"""
# 3. Paths in Graphs

In graph theory, a [path](https://en.wikipedia.org/wiki/Path_(graph_theory))
is a sequence of non-repeating nodes such that from each of its nodes there is an edge to 
the next. Path-related measure provide a sense of the magnitude of a graph, in terms of distances between nodes.

Chapter contents:

- [Shortest Paths](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.shortest_path_length.html#networkx.algorithms.shortest_paths.generic.shortest_path_length)
- [Average Shortest Path Distribution]()
- [Diameter](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.diameter.html#networkx.algorithms.distance_measures.diameter)
- [Eccentricity](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.eccentricity.html#networkx.algorithms.distance_measures.eccentricity)
- [Radius](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.radius.html#networkx.algorithms.distance_measures.radius)
- [Periphery](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.periphery.html#networkx.algorithms.distance_measures.periphery)
- [Center](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.center.html#networkx.algorithms.distance_measures.center)
""")

st.write(r"""
### 3.1 Shortest Paths

The shortest path between two nodes is the path with the minimum number of edges. Formally, for a graph $G = (V, 
E)$ and two vertices $u, v \in V$, the shortest path from $u$ to $v$ is denoted as $\delta(u, v)$.

Here we compute all shortest paths. Each one of the following metrics uses this computation.

Time complexity: $\mathcal{\Theta}(|V||E|\log(|V|))$ 
""")

dsp.display_shortest_path_length(G)

st.write(r"""
### 3.2 Average Shortest Path Distribution

The average shortest path length of a node is given by the 

$$
L(v) = \frac{1}{|R|} \sum_{u \neq v \in V} \delta(u, v)
$$

where $R$ is the set of reachable nodes $v$ from $u$, denoted as $|u\leadsto v|$
""")

measure_name = 'average_shortest_path_length'
dsp.display_df_and_plot_histogram(G, measure_name)

st.write(r"""
### 3.3 Eccentricity

The eccentricity of a node in a graph is the greatest shortest path length between that node and any other node. For a graph $G = (V, E)$ and a node $v \in V$, the eccentricity is given by:

$$
\text{ecc}(v) = \max_{u \in V} \delta(v, u)
$$
""")

dsp.display_df_and_plot_histogram(G, 'eccentricity')

st.write(r"""
### 3.4 Diameter

The diameter of a graph is the maximum shortest path length between any two nodes in the graph. For a graph $G = (V, E)$, it is given by:

$$
\text{diam}(G) = \max_{u, v \in V} \delta(u, v)
$$

Here a lower bound for the diameter is computed.
""")

dsp.display_metric(G, 'diameter')
st.write("\n")

st.write(r"""
### 3.5 Periphery

The periphery of a graph is the set of nodes with eccentricity equal to the diameter. For a graph $G = (V, E)$, the periphery is given by:

$$
\text{Periphery}(G) = \{v \in V | \text{ecc}(v) = \text{diam}(G)\}
$$
""")

dsp.display_df(G, 'periphery')

st.write(r"""
### 3.6 Radius

The radius of a graph is the minimum eccentricity of any node in the graph. For a graph $G = (V, E)$, the radius is given by:

$$
\text{rad}(G) = \min_{v \in V} \text{ecc}(v)
$$
""")

dsp.display_metric(G, 'radius')

st.write(r"""
### 3.7 Center

The center of a graph is the set of nodes with eccentricity equal to the radius. For a graph $G = (V, E)$, the center is given by:

$$
\text{Center}(G) = \{v \in V | \text{ecc}(v) = \text{rad}(G)\}
$$
""")

dsp.display_df(undirected_G, 'center')  # TODO: Does not provide good results yet

