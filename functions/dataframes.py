import streamlit as st
import pandas as pd


def species_scores_dataframe(species_scores_dict):
    """
    Takes in a dictionary with species and scores and returns a sorted dataframe.
    Example:
    {
    'Vulpes': 19,
    'Corvus': 11,
    'Carbidae': 13
    }
    :param species_scores_dict: dictionary with species as keys and score as values.
    :return: dataframe sorted by score in descending order.
    """
    # Create DataFrame from dictionary
    scores_df = pd.DataFrame(list(species_scores_dict.items()), columns=['Specie', 'Score'])

    # Sort DataFrame in descending order by score
    scores_df = scores_df.sort_values('Score', ascending=False)

    # Reset the index to start from 1
    scores_df.index = range(1, len(scores_df) + 1)

    return scores_df


def subgraphs_dataframe(subgraphs_list):
    """
    Takes in two-dimensional list of subgraphs
    :param subgraphs_list:
    :return:
    """
    subgraph_sizes = [len(subgraph) for subgraph in subgraphs_list]

    sizes_df = pd.DataFrame(subgraph_sizes, columns=["Size"], index=range(1, len(subgraph_sizes) + 1))

    size_counts = sizes_df['Size'].value_counts().reset_index()

    size_counts.columns = ['Size', 'Count']

    size_counts = size_counts.sort_values('Size', ascending=True)

    size_counts['Size'] = size_counts['Size'].astype(str)
    return size_counts


def species_dataframe(measure_name, subgraphs_df):
    # Create a list of tuples (component index, component size)
    component_sizes = [(i, len(component)) for i, component in enumerate(st.session_state[measure_name])]

    # Sort components by size in descending order
    component_sizes.sort(key=lambda x: x[1], reverse=True)

    # Generate options based on the sorted list of component sizes
    options = [f'Component {i+1} (Size = {component[1]})' for i, component in enumerate(component_sizes)]

    # Now the selected_option gives the index in the sorted list
    selected_option = st.selectbox('Select a component:', options)

    # Extract component index from the selected option
    sorted_component_index = int(selected_option.split()[1]) - 1

    # Use the sorted_component_index to retrieve the component_index from the component_sizes list
    component_index, component_size = component_sizes[sorted_component_index]

    # Get the species list for the selected component
    species_list = st.session_state[measure_name][component_index]
    species_df = pd.DataFrame(species_list, columns=['Species'], index=range(1, len(species_list) + 1))

    col1, col2 = st.columns([1, 1.05])
    with col1:
        st.dataframe(species_df, height=246, width=330)
    with col2:
        st.markdown(
            f'<div style="border: 1px solid #CCCCCC; padding: 2% 0% 0% 2%; border-radius: 5px;">'
            f'<p style="font-size: 14px;">Size:</p>' # of {selected_option}
            f'<p style="font-size: 36px;">{component_size}</p>'
            '</div>', unsafe_allow_html=True
        )
        """
        st.markdown(
            f'<div style="border: 1px solid #CCCCCC; padding: 2% 0% 0% 2%; border-radius: 5px; background-color: #7c8477;">'
            f'<p style="font-size: 14px;">Size of {selected_option}:</p>'
            f'<p style="font-size: 36px;">{component_size}</p>'
            '</div>', unsafe_allow_html=True
        )
        """


def species_text_area(measure_name):
    options = [f'Component {i} (size: {len(component)})' for i, component in enumerate(st.session_state[measure_name])]
    selected_option = st.selectbox('Select a component:', options)

    component_index = options.index(selected_option)
    species_list = ''.join(f'{species}\n' for species in st.session_state[measure_name][component_index])

    st.text_area('Species:', species_list, height=150)