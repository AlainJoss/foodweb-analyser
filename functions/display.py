import streamlit as st
import pandas as pd
import numpy as np
from functions.plots import histogram, bar_plot
from functions.algorithms import graph_algorithm
from functions.dataframes import species_scores_dataframe, subgraphs_dataframe, species_dataframe, species_text_area
from functions.streamlit_elements import create_session_state, form_and_submit_button, init_session_state
from functions.timer import display_elapsed_time, start_time, end_time


def display_shortest_path_length(graph):
    measure_name = 'shortest_path_length'
    create_session_state(measure_name)
    form_and_submit_button(graph, measure_name)

    if st.session_state[f"{measure_name}"] is not None:

        # Add a selectbox for the user to select a specie
        init_session_state('species', list(graph.nodes))
        selected_species = st.selectbox('Enter or select a species:', options=sorted(st.session_state['species']))

        if selected_species:
            # Fetch the sub-dictionary corresponding to the selected species
            single_specie_dict = st.session_state[f"{measure_name}"][selected_species]

            scores_df = species_scores_dataframe(single_specie_dict)
            col1, col2 = st.columns([1, 1.05])
            with col1:
                st.dataframe(scores_df, height=245, width=330)
            with col2:
                avg_score = np.mean(scores_df['Score'])  # average st.session_state[f"{measure_name}"]
                avg_score = round(float(avg_score), 5)
                st.markdown(
                    f'<div style="border: 1px solid #CCCCCC; padding: 2% 0% 0% 2%; border-radius: 5px;">'
                    f'<p style="font-size: 14px;">Average {measure_name.replace("_", " ").capitalize()}:</p>'
                    f'<p style="font-size: 26px;">{avg_score}</p>'
                    '</div>', unsafe_allow_html=True
                )

            fig = histogram(measure_name)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("Please enter or select a valid species.")


def display_df(graph, measure_name):
    create_session_state(measure_name)
    form_and_submit_button(graph, measure_name)

    if st.session_state[f"{measure_name}"] is not None:
        scores_df = species_scores_dataframe(st.session_state[f"{measure_name}"])
        col1, col2 = st.columns([1, 1.05])
        with col1:
            st.dataframe(scores_df, height=246, width=330)
        with col2:
            avg_score = np.mean(scores_df['Score']) # average st.session_state[f"{measure_name}"]
            avg_score = round(float(avg_score), 5)
            st.markdown(
                f'<div style="border: 1px solid #CCCCCC; padding: 2% 0% 0% 2%; border-radius: 5px;">'
                f'<p style="font-size: 14px;">Average {measure_name.replace("_", " ").capitalize()}:</p>'
                f'<p style="font-size: 26px;">{avg_score}</p>'
                '</div>', unsafe_allow_html=True
            )


def display_df_and_plot_histogram(graph, measure_name):
    start_t = start_time()
    create_session_state(measure_name)
    form_and_submit_button(graph, measure_name)
    end_t = start_time()
    display_elapsed_time(start_t, end_t)
    if st.session_state[f"{measure_name}"] is not None:
        scores_df = species_scores_dataframe(st.session_state[f"{measure_name}"])
        col1, col2 = st.columns([1, 1.05])
        with col1:
            st.dataframe(scores_df, height=246, width=330)
        with col2:
            avg_score = np.mean(scores_df['Score']) # average st.session_state[f"{measure_name}"]
            avg_score = round(float(avg_score), 5)
            st.markdown(
                f'<div style="border: 1px solid #CCCCCC; padding: 2% 0% 0% 2%; border-radius: 5px;">'
                f'<p style="font-size: 14px;">Average {measure_name.replace("_", " ").capitalize()}:</p>'
                f'<p style="font-size: 26px;">{avg_score}</p>'
                '</div>', unsafe_allow_html=True
            )
    
        fig = histogram(measure_name)

        st.plotly_chart(fig, use_container_width=True)


def display_df_and_plot_bar(graph, measure_name):
    start_t = start_time()
    create_session_state(measure_name)
    form_and_submit_button(graph, measure_name)
    end_t = start_time()
    display_elapsed_time(start_t, end_t)
    if st.session_state[f"{measure_name}"] is not None:
        subgraphs_df = subgraphs_dataframe(st.session_state[f"{measure_name}"])

        species_dataframe(measure_name, subgraphs_df)

        with st.container():
            fig = bar_plot(subgraphs_df)
            st.plotly_chart(fig, use_container_width=True)


def display_species_dataframe(graph, measure_name, element_type='nodes'):
    create_session_state(measure_name)
    form_and_submit_button(graph, measure_name)
    if st.session_state[f"{measure_name}"] is not None:
        elements_df = None
        if element_type == 'nodes':
            elements_df = pd.DataFrame(st.session_state[measure_name], columns=[element_type.capitalize()])
        elif element_type == 'edges':
            elements_df = pd.DataFrame(st.session_state[measure_name], columns=['Source', 'Target'])
        if elements_df is not None:
            col1, col2 = st.columns([1, 1.05])
            with col1:
                st.dataframe(elements_df, height=50, width=330)
            with col2:
                st.markdown(
                    f'<div style="border: 1px solid #CCCCCC; padding: 2% 0% 0% 2%; border-radius: 5px;">'
                    f'<p style="font-size: 14px;">{measure_name.replace("_", " ").capitalize()}:</p>'
                    f'<p style="font-size: 36px; ">{len(elements_df)}</p>'
                    '</div>', unsafe_allow_html=True
                )


def display_multiple_metrics_and_dataframes(graph, measure_names, num_columns):
    for measure_name in measure_names:
        create_session_state(measure_name)

    with st.form(key=f"{'-'.join(measure_names)}-Form"):
        submit_button = st.form_submit_button(label="Compute")

    if submit_button:
        with st.spinner('This will take a few seconds ... stay tuned'):
            for measure_name in measure_names:
                st.session_state[f"{measure_name}"] = graph_algorithm(graph, measure_name)

    # Check if the last measure_name exists in the session_state
    if st.session_state[f"{measure_names[-1]}"] is not None:
        cols = st.columns(num_columns)
        for i in range(num_columns):
            with cols[i]:
                species_list = st.session_state[measure_names[i]]
                species_df = pd.DataFrame(species_list, columns=[measure_names[i].replace("_", " ").capitalize()])
                st.markdown(
                    f'<div style="border: 1px solid #CCCCCC; padding: 0.5%; border-radius: 5px;">'
                    f'<p style="font-size: 14px; margin-bottom: 0;">&nbsp;{measure_names[i].replace("_", " ").capitalize()}:</p>'
                    f'<p style="font-size: 30px; text-align: center; margin-top: 0; margin-bottom: 5px;">{len(species_list)}</p>'
                    '</div>', unsafe_allow_html=True
                )
                st.write("\n")
                st.dataframe(species_df, height=246, width=250)


def display_metric(graph, measure_name, percentage=False):
    start_t = start_time()
    key = f'{measure_name}'
    create_session_state(measure_name)
    form_and_submit_button(graph, measure_name)
    end_t = start_time()
    display_elapsed_time(start_t, end_t)
    if st.session_state[key] is not None:
        if percentage:
            formatted_score = f"{round(st.session_state[key] * 100, 5)}%"
        else:
            formatted_score = f"{round(st.session_state[key], 5)}"

        st.markdown(
            f'<div style="border: 1px solid #CCCCCC; padding: 2% 0% 0% 2%; border-radius: 5px;">'
            f'<p style="font-size: 14px;">{measure_name.replace("_", " ").capitalize()}:</p>'
            f'<p style="font-size: 36px; ">{formatted_score}</p>'
            '</div>', unsafe_allow_html=True
        )


