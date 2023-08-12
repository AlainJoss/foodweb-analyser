import streamlit as st
from functions import display as dsp

# TODO: DISPLAY THE NODE AND EDGE CUT METRICS

G, undirected_G = st.session_state.G, st.session_state.undirected_G

@st.cache_resource
def display_connectivity():

    st.write(r"""
    # 1. Connectivity 

    In graph theory, [connectivity](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)) 
    refers to various properties of a graph related to the existence of paths between nodes. 

    Chapter contents:

    - [Density](https://networkx.org/documentation/stable/reference/generated/networkx.classes.function.density.html)
    - Graph Components
        - [Weakly Connected Components]((https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.components.weakly_connected_components.html#networkx.algorithms.components.weakly_connected_components))
        - [Strongly Connected Components](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.components.strongly_connected_components.html#networkx.algorithms.components.strongly_connected_components)
    - Minimum Cut
        - [Minimum Node Cut]((https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.connectivity.cuts.minimum_node_cut.html))
        - [Minimum Edge Cut](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.connectivity.cuts.minimum_edge_cut.html#networkx.algorithms.connectivity.cuts.minimum_edge_cut)
    """)

display_connectivity()

@st.cache_resource
def display_density():

    st.write(r"""
    ### 1.1 Density 

    Density is a measure of the overall connectivity in a graph, defined as the ratio of the number of actual edges to 
    the maximum possible number of edges. For an undirected graph $G = (V, E)$, density $D$ is given by:

    $$
    D = \frac{|E|}{|V|(|V| - 1)}
    $$

    A high density indicates a dense graph with a high number of interactions between nodes.

    Time complexity: $\mathcal{\Theta}(1)$ 
    """)

display_density()

metric = "density"
dsp.display_metric(G, metric, percentage=True)
st.write("\n")

@st.cache_resource
def display_graph_components():

    st.write(r"""
    ### 1.2 Graph Components 

    A graph component is a maximal connected subgraph within a graph. For directed graphs, there are two types of components: Weakly Connected Components (WCC) and Strongly Connected Components (SCC).
    """)

    st.write(r"""
    #### 1.2.1 Weakly Connected Components

    A WCC in a directed graph $G = (V, E)$ is a maximal connected subgraph $H = (V', E')$ where $V' \subseteq V$ and $E' \subseteq E$ such that for every pair of vertices $u, v \in V'$, there exists an undirected path from $u$ to $v$.

    If there are multiple WCCs the graph is disconnected.

    Time complexity $\mathcal{\Theta}(|V| + |E|)$
    """)

display_graph_components()

dsp.display_df_and_plot_bar(G, 'weakly_connected_components')

st.write(r"""
#### 1.2.2 Strongly Connected Components

An SCC in a directed graph $G = (V, E)$ is a maximal connected subgraph $H = (V', E')$ where $V' \subseteq V$ and $E' \subseteq E$ such that for every pair of vertices $u, v \in V'$, there exists a directed path from $u$ to $v$.

The presence of multiple SCCs implies a division of the graph into clusters.

Time complexity $\mathcal{\Theta}(|V| + |E|)$
""")
dsp.display_df_and_plot_bar(G, 'strongly_connected_components')

# TODO: rewrite the function for the text area. Display edges, not nodes.
# TODO: rewrite the cut explanations mathematically rigorously.

st.write(r"""
### 1.3 Minimum Cuts

The minimum cut of a graph corresponds to the smallest set of edges or nodes whose removal would break the graph into two or more disconnected components. A minimum cut is not always unambiguous, that is, there can be multiple minimum cuts, which have all the same cardinality. It is a measure of the robustness of the network against node or edge removal.

""")
st.write(r"""
#### 1.3.1 Minimum Node Cut
The minimum node cut is defined as the smallest set of nodes, $S$, that upon removal results in a disconnected graph. Formally, for a connected graph $G = (V, E)$, we can represent the minimum node cut as follows:

$$
S = \arg\min_{S' \subseteq V} \{|S'| : G - S' \text{ is disconnected}\}
$$


In the above expression, $G - S'$ represents the graph resulting from the removal of nodes in set $S'$ from $G$. The cardinality $|S|$ is referred to as the node connectivity of the graph. 

Time complexity: $\mathcal{O}(|V||E|)$.
""")

measure_name = 'minimum_node_cut'
dsp.display_species_dataframe(undirected_G, measure_name)

st.write(r"""
#### 1.3.2 Minimum Edge Cut
The minimum edge cut is defined as the smallest set of edges, $C$, that upon removal results in a disconnected graph. Formally, for a connected graph $G = (V, E)$, we can represent the minimum edge cut as follows:

$$
C = \arg\min_{C' \subseteq E} \{|C'| : G - C' \text{ is disconnected}\}
$$

In the above expression, $G - C'$ represents the graph resulting from the removal of edges in set $C'$ from $G$. The cardinality $|C|$ is referred to as the edge connectivity of the graph.

Time complexity: $\mathcal{O}(|V||E|)$.
""")

measure_name = 'minimum_edge_cut'
dsp.display_species_dataframe(undirected_G, measure_name, 'edges')

