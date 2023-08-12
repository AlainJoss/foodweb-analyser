import streamlit as st
from functions import display as dsp

G = st.session_state.G

st.write("""
# 5. Trophic Structure

Trophic structure measures provide insights into the topology and organization of ecological networks, such as food webs. These metrics can help to understand the distribution of species across trophic levels and the overall stability of the ecosystem. In this chapter, we discuss key trophic structure metrics for directed graphs: trophic levels, omnivory index, and the proportion of each trophic level.
""")


st.write("""
### 5.1 Distinctive Species

Among distinctive species we identify basal species, apex predators, and cannibal species. Formally, basal species are nodes with an 
in-degree of 0, apex predators are nodes with an out-degree of 0, and cannibal species are nodes with self-loops.
""")

# TODO: Include onion layers, omnivore index

measure_names = ['basal_species', 'apex_predators', 'cannibal_species']
dsp.display_multiple_metrics_and_dataframes(G, measure_names, num_columns=3)


st.write("""
### 5.1 Trophic Levels

Trophic levels represent the position of a species in the food chain, with primary producers at the base and apex predators at the top.

The trophic level $s(v)$ of a node $v$ in a directed graph is defined as:
""")

st.latex(r'''
s(v) = 1 + \frac{1}{k^{in}_v} \sum_{u} a_{uv}s_u
''')

st.write("""
where $k^{in}_v$ is the in-degree of node $v$, $a_{uv}$ the entries in the adjacency matrix, and $s_u$ the trophic level of predator $u$.

Basal nodes have $k^{in}_v = 0$, they therefore have $s_v = 1$ by convention.

The trophic levels correspond the expected value of the path length from any of the sources to the node $v$. An inefficient, but self explaining algorithm follows these steps:

1.  Provide a directed Graph G.

2.  Calculate the probability function $p_v(k)$ for each node $v$, which represents the probability of obtaining energy over a path of length $k$ from any of the node sources. This can be done by identifying all possible paths of length $k$ from any source to the $i$-th component and computing the product of the branch probabilities (weights) contained in each path. Then, sum up the probabilities of all such paths.

3. Compute the trophic level $x_v$ of the $v$-th node as the expected value of the path length from any of the sources:

    $x_v = \sum_{k=0}^{\infty} k \cdot p_v(k)$

    where the sum is taken over all possible path lengths $k$ (from $0$ to infinity).
""")

measure_name = 'trophic_levels'
dsp.display_df_and_plot_histogram(G, measure_name)

st.write("""
### 5.2 Trophic Cohesion/Stability

Trophic cohesion measures the extent to which nodes at the same trophic level are connected to each other. High trophic cohesion implies a more stable ecosystem, as it indicates a higher degree of redundancy within each trophic level.

Mathematically, the trophic cohesion $TC$ is defined as:
""")

st.latex(r'''
TC = \frac{\sum_{i, j \in V} |TL(i) - TL(j)| A_{ij}}{m}
''')

st.write("""
where $V$ is the set of nodes, $A_{ij}$ is the adjacency matrix, and $m$ is the total number of edges in the network.
""")

measure_name = 'trophic_incoherence'
dsp.display_metric(G, measure_name)

st.write("""
### 5.3 Omnivory Index
""")
