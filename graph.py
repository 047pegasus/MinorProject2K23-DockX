import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

def plot_real_time_cpu_usage():
    # Initialize the figure and axis
    fig, ax = plt.subplots(figsize=(10, 3))
    fig.set_size_inches(10, 3)  # Set the size of the plot window
    ax.set_facecolor('#1F1E2E')  # Set the plot background color

    # Set up the initial plot
    num_points = 60  # Number of data points to show initially (15 seconds with 0.25-second intervals)
    x = np.arange(num_points) * 0.25  # Time axis in seconds
    y = np.zeros((5, num_points))  # Empty array for CPU usage of each container

    # Define a modern and aesthetic color palette
    palette = ['#EF476F', '#FFD166', '#06D6A0', '#118AB2', '#073B4C']

    lines = [ax.plot(x, y[i], color=palette[i])[0] for i in range(5)]
    ax.set_ylim(0, 100)  # Set y-axis limits for CPU usage percentage
    ax.set_xticks([])  # Hide x-axis ticks and labels
    ax.spines['top'].set_visible(False)  # Remove top border
    ax.spines['right'].set_visible(False)  # Remove right border
    ax.spines['bottom'].set_visible(False)  # Remove bottom border
    ax.spines['left'].set_visible(False)  # Remove left border
    ax.yaxis.grid(True, color='white', linestyle='solid', linewidth=0.5)  # Add horizontal grid lines
    ax.xaxis.set_tick_params(color='white')  # Set x-axis tick color to white
    ax.yaxis.set_tick_params(color='white')  # Set y-axis tick color to white
    plt.setp(ax.spines.values(), color='white')  # Set color of all spines to white
    plt.setp(ax.xaxis.get_ticklines(), color='white')  # Set color of x-axis tick lines to white
    plt.setp(ax.yaxis.get_ticklines(), color='white')  # Set color of y-axis tick lines to white
    ax.xaxis.label.set_color('white')  # Set color of x-axis label to white
    ax.yaxis.label.set_color('white')  # Set color of y-axis label to white

    plt.ion()  # Enable interactive mode for real-time updating

    while True:
        # Generate random CPU usage values for the containers
        cpu_usage = np.random.uniform(0, 100, size=(5,))

        # Shift the existing data to the left and append new data
        y = np.hstack((y[:, 1:], cpu_usage[:, np.newaxis]))
        x = np.arange(num_points) * 0.25  # Update x with the new range

        # Update the plot with the new data and apply smoothing
        for i, line in enumerate(lines):
            x_smooth = np.linspace(x.min(), x.max(), 300)  # Generate a smooth time axis
            y_smooth = make_interp_spline(x, y[i])(x_smooth)  # Apply spline interpolation to smooth the curve
            line.set_data(x_smooth, y_smooth)

        # Adjust the x-axis limits to hold data for at most 15 seconds
        ax.set_xlim(x[-1] - 15, x[-1])

        # Add legend outside the plot
        ax.legend(lines, [f'Container {i+1}' for i in range(5)], loc='lower left', bbox_to_anchor=(1.02, 1))

        # Update the figure canvas
        fig.canvas.draw()
        fig.canvas.flush_events()

        # Pause for a shorter duration to control the refresh rate
        plt.pause(0.06)


# Call the function to start plotting real-time CPU usage
plot_real_time_cpu_usage()
