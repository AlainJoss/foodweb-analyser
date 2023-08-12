import networkx as nx
import streamlit as st
import numpy as np

import time
import time

def graph_algorithm(graph, algorithm):
    algorithm_funcs = {
        'in_degree': lambda g: dict(g.in_degree()),
        'out_degree': lambda g: dict(g.out_degree()),
        'total_degree': lambda g: dict(g.degree()),
        'node_betweenness': lambda g: nx.betweenness_centrality(g, normalized=False),
        'edge_betweenness': lambda g: nx.edge_betweenness_centrality(g, normalized=False),
        'inward_closeness': lambda g: nx.closeness_centrality(g),
        'outward_closeness': lambda g: nx.closeness_centrality(g),
        'pagerank': nx.pagerank,
        'local_clustering_coefficient': nx.clustering,
        'weakly_connected_components': lambda g: list(nx.weakly_connected_components(g)),
        'strongly_connected_components': lambda g: list(nx.strongly_connected_components(g)),
        'density': nx.density,
        'global_clustering_coefficient': global_clustering_coefficient,
        'trophic_incoherence': nx.trophic_incoherence_parameter,
        'trophic_levels': nx.trophic_levels,
        'node_connectivity': nx.node_connectivity,
        'edge_connectivity': nx.edge_connectivity,
        'minimum_node_cut': lambda g: list(compute_minimum_node_cut(g)),
        'minimum_edge_cut': nx.minimum_edge_cut,
        'apex_predators': apex_predators,
        'basal_species': basal_species,
        'cannibal_species': cannibal_species,
        'shortest_path_length': lambda g: dict(nx.shortest_path_length(g)),  # updated line
        'average_shortest_path_length': average_shortest_path_length,
        'diameter': diameter,
        'find_cliques': find_cliques,
        'max_clique': nx.approximation.max_clique,
        'node_clique_number': nx.node_clique_number,
        'k_core': k_core,
        'core_number': nx.core_number,
        'onion_layers': nx.onion_layers,
        'bridges': nx.bridges,
        'eccentricity': eccentricity,
        'radius': radius,
        'periphery': periphery,
        'center': center,
    }

    if algorithm not in algorithm_funcs:
        raise ValueError(f"Invalid algorithm: {algorithm}")

    return algorithm_funcs[algorithm](graph)


def compute_minimum_node_cut(g):
    if nx.is_connected(g):
        return nx.minimum_node_cut(g)
    else:
        st.warning("Graph is already disconnected!")
        return []  # This will return an empty list


def global_clustering_coefficient(graph):
    if st.session_state['local_clustering_coefficient'] is None:
        st.warning("Before computing the GCC, compute the LCCs.")
        return 0
    else:
        local_scores = list(st.session_state['local_clustering_coefficient'].values())
        gcc = np.average(local_scores)
        # Save to session state
        st.session_state['global_clustering_coefficient'] = gcc
        return gcc


def apex_predators(graph):
    apex_species = sorted({n for n, d in graph.out_degree() if d == 0})
    return apex_species


def basal_species(graph):
    basal_species = sorted({k for k, d in graph.in_degree() if d == 0})
    return basal_species


def cannibal_species(graph):
    cannibal_species = sorted(node for node in nx.nodes_with_selfloops(graph))
    return cannibal_species


def average_shortest_path_length(graph):
    averages = {node: np.mean(list(paths.values())) for node, paths in
                st.session_state['shortest_path_length'].items()}
    return averages


def eccentricity(graph):
    ecc = {node: np.max(list(paths.values())) for node, paths in
           st.session_state['shortest_path_length'].items()}
    return ecc


def diameter(graph):
    diameter = np.max([max(paths.values()) for paths in
                       st.session_state['shortest_path_length'].values()])
    return diameter


# TODO: function is broken
def radius(graph):
    ecc = {node: np.max(list(paths.values())) for node, paths in
           st.session_state['shortest_path_length'].items()}
    radius = np.min(ecc)
    return radius


def periphery(graph):
    shortest_path_lengths = st.session_state['shortest_path_length']

    # Calculate the eccentricity of each node
    eccentricities = {node: max(paths.values()) for node, paths in shortest_path_lengths.items()}

    # Calculate the diameter of the graph
    diameter = max(eccentricities.values())

    # Identify the periphery nodes (those with eccentricity equal to the diameter)
    periphery_nodes = {node: ecc for node, ecc in eccentricities.items() if ecc == diameter}

    return periphery_nodes


def center(graph):
    shortest_path_lengths = st.session_state['shortest_path_length']

    # Calculate the eccentricity of each node
    eccentricities = {node: max(paths.values()) for node, paths in shortest_path_lengths.items()}
    eccentricities = {node: ecc for node, ecc in eccentricities.items() if ecc > 0}

    # Calculate the diameter of the graph
    radius = min(eccentricities.values())

    # Identify the periphery nodes (those with eccentricity equal to the diameter)
    center_nodes = {node: ecc for node, ecc in eccentricities.items() if ecc == radius}

    return center_nodes


def k_core():
    diameter = 404
    if st.session_state['shortest_path_length'] is not None:
        diameter = np.max([max(paths.values()) for paths in st.session_state['shortest_path_length'].values()])
    return diameter


def find_cliques(graph):
    return dict(nx.find_cliques(st.session_state.undirected_G))
