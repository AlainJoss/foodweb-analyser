import streamlit as st
from functions.algorithms import graph_algorithm


def create_session_state(name):
    if f'{name}' not in st.session_state:
        st.session_state[f'{name}'] = None


def init_session_state(name, obj):
    create_session_state(name)
    if st.session_state[f'{name}'] is None:
        st.session_state[f'{name}'] = obj


def form_and_submit_button(graph, measure_name):
    with st.form(key=f"{measure_name.capitalize()}-Form"):
        submit_button = st.form_submit_button(label="Compute")
        css = r'''
        <style>
            [data-testid="stForm"] {border: 0px}
        </style>
        '''
        st.markdown(css, unsafe_allow_html=True)

    # Initialize session state regardless of whether the button is pressed
    if measure_name not in st.session_state:
        init_session_state(measure_name, None)

    if submit_button:
        with st.spinner('This will take a few seconds ... stay tuned'):
            init_session_state(measure_name, graph_algorithm(graph, measure_name))
