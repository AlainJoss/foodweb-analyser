import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

G, undirected_G = st.session_state.G, st.session_state.undirected_G


def visualize_network(G, plot_options):
    pos = nx.spring_layout(G, iterations=20, seed=1721)
    fig, ax = plt.subplots(figsize=(40, 15), dpi=10000)  # Increase dpi here
    ax.axis("off")
    nx.draw_networkx(G, pos=pos, ax=ax, **plot_options)
    st.pyplot(fig)


plot_options = {
    'node_color': 'blue',
    'node_size': 1000,
    'edge_color': 'gray',
    'linewidths': 0,
    'width': 100,
    'with_labels': True
}

# Visualize the network
visualize_network(G, plot_options)

