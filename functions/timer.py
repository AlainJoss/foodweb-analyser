import time
import streamlit as st

def start_time():
    return time.time()

def end_time():
    return time.time()

def display_elapsed_time(start_t, end_t):
    et = end_t - start_t
    st.write(f'**Elapsed Time**: {round(et, 3)} s')