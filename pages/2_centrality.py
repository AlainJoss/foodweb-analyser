import streamlit as st
from functions import display as dsp

G = st.session_state.G

@st.cache_resource
def display_centrality():
    st.write("""
    # 2. Centrality

    In graph theory, [centrality](https://en.wikipedia.org/wiki/Centrality)
    measures quantify the relative importance of nodes in a graph. 

    Chapter contents:
    - degree centrality
        - [in-degree](https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.in_degree.html)
        - [out-degree](https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.out_degree.html)
        - [degree](https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.degree.html)
    - betweenness centrality
        - [node betweenness centrality](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.betweenness_centrality.html#networkx.algorithms.centrality.betweenness_centrality)
        - [edge betweenness centrality](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.betweenness_centrality.html#networkx.algorithms.centrality.betweenness_centrality)
    - closeness centrality
        - [inward closeness centrality](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.closeness_centrality.html#networkx.algorithms.centrality.closeness_centrality)
        - [outward closeness centrality](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.closeness_centrality.html#networkx.algorithms.centrality.closeness_centrality)
    - [pagerank](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html)
    """)

display_centrality()

@st.cache_resource
def display_in_degree_centrality():
    st.write(r"""
    ### 2.1 Degree Centrality 
    The degree of a node is the number of edges connected to that node. In directed graphs, in-degree, out-degree, and total-degree are distinguished.

    #### 2.1.1 In-degree

    The in-degree of a node in a directed graph is the number of incoming edges. Formally, the in-degree of a node $i$ is defined as:

    $$
    \text{In-degree}(i) = \sum_{j=1}^{|V|} A_{ji}
    $$

    where $A_{ji}$ is the adjacency matrix entry for the directed edge from node $(j,i)$.

    Time complexity: $\mathcal{\Theta}(|V|)$ 
    """)

display_in_degree_centrality()
centrality_type = 'in_degree'
dsp.display_df_and_plot_histogram(G, centrality_type)

@st.cache_resource
def display_out_degree_centrality():
    st.write(r"""
    #### 2.1.2 Out-degree

    The out-degree of a node in a directed graph is the number of outgoing edges. Formally, the out-degree of a node $i$ is defined as:

    $$
    \text{Out-degree}(i) = \sum_{j=1}^{|V|} A_{ij}
    $$

    where $A_{ij}$ is the adjacency matrix entry for the directed edge $(i,j)$.

    Time complexity: $\mathcal{\Theta}(|V|)$ 
    """)

display_out_degree_centrality()
centrality_type = 'out_degree'
dsp.display_df_and_plot_histogram(G, centrality_type)

@st.cache_resource
def display_total_degree_centrality():
    st.write(r"""
    #### 2.1.3 Total-Degree

    The total-degree of a node in a directed graph is the sum of its in-degree and out-degree. Formally, the total-degree of a node $i$ is defined as:

    $$
    \text{Total-Degree}(i) = \text{In-degree}(i) + \text{Out-degree}(i)
    $$

    where $A_{ji}$ is the adjacency matrix element for the directed edge from node $j$ to node $i$, and $A_{ij}$ is the adjacency matrix element for the directed edge from node $i$ to node $j$.

    Time complexity: $\mathcal{\Theta}(|V|)$ 
    """)

display_total_degree_centrality()
centrality_type = 'total_degree'
dsp.display_df_and_plot_histogram(G, centrality_type)

@st.cache_resource
def display_betwenness_centrality():
    st.write(r"""
    ### 2.2 Betweenness Centrality

    Betweenness centrality measures the extent to which a node lies on paths between other nodes. Nodes with high betweenness centrality have a large influence on the transfer of energy through the graph, under the assumption that the energy transfer follows the shortest paths.
    """)

    st.write(r"""
    #### 2.2.1 Node Betweenness Centrality

    Node betweenness centrality quantifies the number of times a node acts as a bridge along the shortest path between two other nodes. It is computed as:

    $$
    C_{B}(v) =\sum_{s,t \in V} \frac{\sigma(s, t|v)}{\sigma(s, t)}
    $$

    where $V$ is the set of nodes, $\sigma(s, t)$ is the total number of shortest paths from node $s$ to node $t$, and $\sigma(s, t|v)$ is the number of those paths that pass through $v$.

    Time complexity: $\mathcal{O}(|V|\cdot|E|)$ (should take few seconds but actually takes up to 15 minutes, because of 
    the implementation.) 
    """)

display_betwenness_centrality()
centrality_type = 'node_betweenness'  # Brandes
dsp.display_df_and_plot_histogram(G, centrality_type)

@st.cache_resource
def display_edge_betwenness_centrality():
    st.write(r"""
    #### 2.2.2 Edge Betweenness Centrality

    Edge betweenness centrality quantifies the number of times an edge acts as a bridge along the shortest path between two other nodes. It is computed as:

    $$
    C_{B}(e) =\sum_{s,t \in V} \frac{\sigma(s, t|e)}{\sigma(s, t)}
    $$

    where $V$ is the set of nodes, $e$ is an edge, $\sigma(s, t)$ is the total number of shortest paths from node $s$ to node $t$, and $\sigma(s, t|e)$ is the number of those paths that pass through $e$.

    Time complexity: $\mathcal{O}(|V|\cdot|E|)$ (should take few seconds but actually takes up to 15 minutes, because of 
    the implementation.) 
    """)

display_edge_betwenness_centrality()
centrality_type = 'edge_betweenness'  # Brandes for unweighted graphs
dsp.display_df_and_plot_histogram(G, centrality_type)

@st.cache_resource
def display_inward_closeness_centrality():
    st.write(r"""
    ### 2.3 Closeness Centrality

    Closeness centrality is a measure of the degree to which an individual is near all other individuals in a network.

    #### 2.3.1 Inward Closeness Centrality

    For a directed graph, Inward Closeness Centrality measures the average shortest path from all other nodes to the node in question. It is computed as:

    $$
    C_{in}(v) = \frac{|V| - 1}{\sum_{u}d(u, v)}
    $$

    where $d(u, v)$ is the shortest-path distance from $u$ to $v$.

    Time complexity: $\mathcal{O}(|V|\cdot|E|)$ 
    """)

display_inward_closeness_centrality()
centrality_type = 'inward_closeness'
dsp.display_df_and_plot_histogram(G, centrality_type)

@st.cache_resource
def display_outward_closeness_centrality():
    st.write(r"""
    #### 2.3.2 Outward Closeness Centrality

    For a directed graph, Outward Closeness Centrality measures the average shortest path from the node in question to all other nodes. It is computed as:

    $$
    C_{out}(v) = \frac{|V| - 1}{\sum_{u}d(v, u)}
    $$

    where $d(v, u)$ is the shortest-path distance from $v$ to $u$.

    Time complexity: $\mathcal{O}(|V|\cdot|E|)$
    """)

display_inward_closeness_centrality()
centrality_type = 'outward_closeness'
dsp.display_df_and_plot_histogram(G.reverse(), centrality_type) # reverse G to compute outward closeness

@st.cache_resource
def display_pagerank_centrality():
    st.write(r"""
    ### 2.4 Pagerank Centrality

    Pagerank is a popularity measure designed by Google's founders. It is a way of deciding a page's importance based on the incoming links from other pages. Every web page that links to another page is essentially casting a vote for the other page. The more votes that are cast for a page, the more important the page is assumed to be. It is computed as:

    $$
    PR(p_i) = \frac{1-d}{|E|} + d \sum_{p_j \in M(p_i)} \frac{PR(p_j)}{L(p_j)}
    $$

    where $PR(p_i)$ is the PageRank of page $i$, $d$ is a damping factor (usually set to 0.85), $M(p_i)$ is the set of pages that link to page $i$, and $L(p_j)$ is the number of outbound links on page $j$.

    Time complexity: $\mathcal{O}(|V|+|E|)$
    """)

display_pagerank_centrality()
centrality_type = 'pagerank'
dsp.display_df_and_plot_histogram(G, centrality_type)
