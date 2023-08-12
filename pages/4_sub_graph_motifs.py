import streamlit as st
from functions import display as dsp

G = st.session_state.G

# GCC = number of actual triangles over possible triangles

# TODO: always include if the metric is computed for the directed or undirected version of the graph

# TODO: Fuse with subgraph characterization

st.write("""
# 4. Sub-graph Motifs

Clustering metrics are used to analyze the organization and interconnectedness of nodes in a network. These metrics can provide insights into the network's overall structure and reveal potential functional groups or communities.

(https://networkx.org/documentation/stable/reference/algorithms/clique.html) 
""")

st.write(r"""
### 4.1 Local Clustering Coefficient

The local clustering coefficient for a node measures the proportion of its neighbors that are also connected to each other. It provides an indication of the extent to which nodes in the immediate vicinity of a given node are connected. In the undirected version of the network, the local clustering coefficient $LCC(v)$ for node $v$ is defined as:


$$
LCC(v) = \frac{T(v)}{{2 \text{{deg}}(v) (\text{{deg}}(v) - 1) - 2 deg_{\leftrightarrow}(v)}}
$$

where $deg(v)$ is the degree of node $v$ (the number of incoming and outgoing edges), and $T(v)$ is the number of triangles in which node $v$ is involved.

The global clustering coefficient (GCC) is the average of the local clustering coefficients, while it is also the 
number of actual triangles, over the possbile triangles in the graph. Formally, $GCC$ is defined as:

$$
GCC = \frac{1}{n} \sum_{v=1}^{n} LCC(v)
$$
 
 """)

measure = 'local_clustering_coefficient'
dsp.display_df_and_plot_histogram(G, measure)

st.write(r"""
### 5.1 K-Clique 
A k-clique in a graph $G = (V, E)$ is a maximal complete subgraph $H = (V', E')$, where $V' \subseteq V$ and $E'
\subseteq E$, such that $|V'| = k$, and $\forall u, v \in V'$, if $u \neq v$ then $(u, v) \in E'$. This means that
every pair of distinct vertices in the k-clique is adjacent.

Used algorithms:

- [max_clique](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.approximation.clique.max_clique.html#networkx.algorithms.approximation.clique.max_clique) 
(approx) in $\mathcal{O}(\frac{n}{(\log n)^2})$
- find_cliques
- node_clique_number

Time complexity: $\mathcal{O}(n^2)$
""")

measure_name = 'find_cliques'
dsp.display_df(G, measure_name)

st.write(r"""
### 5.2 [K-Core](https://networkx.org/documentation/stable/reference/algorithms/core.html) 
A k-core in a graph $G = (V, E)$ is a maximal connected induced subgraph $H = (V', E')$, where $V' \subseteq V$ and
$E' \subseteq E$ are such that $\forall v \in V', deg_H(v) \geq k$. Additionally, $\forall e=(u,v) \in E', u,
v \in V'$, meaning all edges in the k-core connect nodes within the k-core.



Used algorithms:
- k_core
- core_number
- onion_layers

Time complexity: $\mathcal{O}(m)$
""")

measure_name = 'k-core'
dsp.display_df_and_plot_histogram(G, measure_name)


