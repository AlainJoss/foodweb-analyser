import streamlit as st
import numpy as np
import plotly.graph_objects as go

# TODO: check why certain histograms have value such as 350k, which do not correspond to the scores


def create_figure(trace, x_title, y_title, x_type='linear', y_type='linear', x_range=None):
    """
    Helper function for both histogram and bar_plot, which generates a figure object using Plotly.

    :param trace: The data trace (e.g., histogram) to be plotted.
    :param x_title: The title of the x-axis.
    :param y_title: The title of the y-axis.
    :param x_type: The type of scale for the x-axis ('linear' or 'log'). Defaults to 'linear'.
    :param y_type: The type of scale for the y-axis ('linear' or 'log'). Defaults to 'linear'.
    :param x_range: The range of values on the x-axis (optional). If not specified, it will be set automatically.
    :return: A Plotly Figure object ready for plotting.
    """

    # Create a new Figure object
    fig = go.Figure(data=[trace])

    # Update the layout to set axis titles, sizing, and margins
    fig.update_layout(
        xaxis=dict(title=x_title, range=x_range, type=x_type),
        yaxis=dict(title=y_title, type=y_type),
        autosize=True,
        width=10,
        bargroupgap=0.1,
        margin=dict(t=10, b=50, r=50, l=50, pad=10)
    )
    return fig


#################### HISTOGRAM


def histogram_params(measure_name, scores_list):
    # Select box value of scale type
    scale_type = st.selectbox(f'Scale Type',
                              ['Standard Scale', 'Log Scale'],
                              key=f'scale_type_{measure_name}', index=0)

    # Slider value of maximum percentile displayed
    percentile_slider = st.slider(f'Maximum Percentile Displayed',
                                  min_value=75, max_value=100, step=1, value=100,
                                  key=f'percentile_slider_{measure_name}')
    
    # Filters out items which are not part of the set quantile
    quantile = np.percentile(scores_list, percentile_slider)

    # Slider value of bins for histogram
    bins_slider = st.slider(f'Histogram Bins',
                            min_value=20, max_value=5000, step=20, value=500,
                            key=f'bins_slider_{measure_name}')

    return scale_type, quantile, bins_slider


def histogram(measure_name):
    """
    This function generates a histogram of scores for a given measure.

    :param measure_name: The name of the measure for which to generate a histogram.
    :param scores_list: A list of scores corresponding to the measure.
    :return: A Plotly Figure object containing the histogram.
    """

    scores_list = list(st.session_state[f'{measure_name}'].values())

    # Get parameters for the histogram
    scale_type, quantile, bins_slider = histogram_params(measure_name, scores_list)

    # Create the histogram trace
    hist_trace = go.Histogram(x=scores_list, nbinsx=bins_slider, marker_color='#7c8477')  # pastel dark green

    # Generate axis titles
    x_title = f"{measure_name.replace('_', ' ').capitalize()}"
    y_title = "Frequency"

    # Determine the range for the x-axis and the type of scale for the y-axis
    x_range = [0.0, quantile]
    y_type = 'log' if scale_type == 'Log Scale' else 'linear'

    # Create the figure
    fig = create_figure(hist_trace, x_title, y_title, x_type='linear', y_type=y_type, x_range=x_range)


    return fig


#################### BAR PLOT

def calculate_bar_width(size_counts, max_bar_width=0.15):
    """
    This function calculates the width for each bar in a bar plot, given the component sizes and a maximum width.

    :param size_counts: A DataFrame containing the sizes and their respective counts.
    :param max_bar_width: The maximum width for each bar. Default is 0.15.
    :return: The width for each bar.
    """

    # Calculate the number of unique component sizes
    num_bars = len(np.unique(size_counts['Size']))

    # Calculate the width for each bar while reserving 10% of the space for gaps
    # If the number of bars is too high, this will cap the width at max_bar_width
    bar_width = min(max_bar_width, (2 - 0.05) / num_bars)

    return bar_width


def bar_plot(size_counts):
    """
    This function generates a bar plot for the counts of each component size.

    :param size_counts: A DataFrame containing the sizes and their respective counts.
    :return: A Plotly Figure object containing the bar plot.
    """

    # Calculate optimal bar width
    bar_width = calculate_bar_width(size_counts, 0.15)

    # Create bar trace
    bar_trace = go.Bar(
        x=size_counts['Size'],  # x position corresponds to 'Size'
        y=size_counts['Count'],  # height of bar corresponds to 'Count'
        text=size_counts['Count'],  # annotate bar with 'Count'
        textposition='outside',  # place annotation outside bar
        marker_color='#7c8477',  # set color of bars
        width=bar_width  # set width of bars
    )

    # Set x-axis and y-axis titles
    x_title = "Component Size"
    y_title = "Count"

    # Generate and return figure
    fig = create_figure(bar_trace, x_title, y_title, x_type='category')

    return fig




