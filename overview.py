import streamlit as st
import networkx as nx
import pandas as pd
from functions.streamlit_elements import create_session_state, init_session_state

# TODO: show list of nodes and edges?
# TODO: cache in functions the md text of each page

# Define the sidebar options
pages = {
    'Overview': 'overview',
    'Connectivity Measures': 'connectivity',
    'Centrality Measures': 'centrality',
    'Path-related Measures': 'path_related',
    'Sub-graph Motifs': 'sub_graph_motifs',
    'Sub-graph Characterization': 'sub_graph_characterization',
    'Trophic Measures': 'trophic'
}


@st.cache_data(show_spinner=False)
def load_data():
    csv_file = "food_webs/01_metaweb.csv"
    edge_df = pd.read_csv(csv_file, low_memory=False)

    G = nx.from_pandas_edgelist(edge_df, source='Source_Name', target='Target_Name', edge_attr=True,
                                create_using=nx.DiGraph())

    undirected_G = G.to_undirected()
    return nx.reverse(G), undirected_G, edge_df


# Home page
st.title("The Food Web of Switzerland")

# Loads data the first time the app is run

with st.spinner("Loading data ... stay tuned"):
    G, undirected_G, edge_df = load_data()

# Session stated for other pages
init_session_state('G', G)
init_session_state('undirected_G', undirected_G)

##### PAGE ######

st.write("""
### Mathematical Representation
This dataset is a representation of Switzerland's food web in the form of a directed graph, 
mathematically denoted as G(V, E, A), where:

-   **V**: Set of nodes, each representing a species in the ecosystem.

-   **E**: Set of edges, each representing a trophic interaction or energy-flow from a prey species (source node) to a predator species (target node).

-   **A**: Set of attributes associated with each edge, containing additional information about the trophic interaction:

    -   **Interaction Type**: PROVIDE EXPLANATION.

    -   **Zone**: PROVIDE EXPLANATION.

    -   **Habitat**: PROVIDE EXPLANATION.
""")

st.write("### Graph Dimensions")

init_session_state('num_nodes', G.number_of_nodes())
init_session_state('num_edges', G.number_of_edges())

col1, col2 = st.columns([1, 3.5])
with col1:
    st.metric("Number of Species", st.session_state['num_nodes'])
with col2:
    st.metric("Number of Trophic Interactions", st.session_state['num_edges'])


st.write("""
### A Random Sample
A glimpse of the data: 5 randomly selected rows (graph edges) of the original data set.
""")
create_session_state('random_sample')
if st.session_state['random_sample'] is None:
    st.session_state['random_sample'] = edge_df.sample(5)
st.dataframe(st.session_state['random_sample'])

st.write("### Species Interactions")

init_session_state('species', list(G.nodes))

selected_species = st.selectbox('Enter or select a species:', options=sorted(st.session_state['species']))

if selected_species:
    in_neighbors = sorted(list(G.predecessors(selected_species)))
    out_neighbors = sorted(list(G.successors(selected_species)))

    # Create dataframes from lists
    in_df = pd.DataFrame(in_neighbors, columns=['Prey'], index=range(1, len(in_neighbors) + 1))
    out_df = pd.DataFrame(out_neighbors, columns=['Predators'], index=range(1, len(out_neighbors) + 1))

    # Create columns for displaying in-neighbors and out-neighbors separately
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Number of Prey", len(in_neighbors))
        st.dataframe(in_df, height=420)

    with col2:
        st.metric("Number of Predators", len(out_neighbors))
        st.dataframe(out_df, height=420)
else:
    st.write("Please enter or select a valid species.")
