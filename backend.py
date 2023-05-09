#Create a Tkinter app to monitor all running docker containers and thier CPU and memory utilization tand plot a realtime graph for the same in the app itself using matplotlib.
import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import docker


# Create a docker client object
client = docker.from_env()

# Create a tkinter window
root = tk.Tk()
root.title("Docker Monitor")
root.geometry("800x600")

# Create a frame for the listbox
frame1 = tk.Frame(root)
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Create a frame for the graph
frame2 = tk.Frame(root)
frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

# Create a listbox to display the running containers
listbox = tk.Listbox(frame1, width=50, height=30)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Create a figure for the graph
fig = plt.figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111)
ax.set_xlabel("Time")
ax.set_ylabel("CPU Usage")
ax.set_title("CPU Usage Monitor")
ax.set_ylim(0, 100)
ax.set_xlim(0, 10)
xs = []
ys = []
line, = ax.plot(xs, ys)

# Create a canvas for the graph
canvas = FigureCanvasTkAgg(fig, master=frame2)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
canvas.draw()

# Function to get the running containers
def get_containers():
    containers = client.containers.list()
    return containers

# Function to get the CPU usage of a container
def get_cpu_usage(container):
    cpu_usage = container.stats(stream=False)["cpu_stats"]["cpu_usage"]["total_usage"]
    return cpu_usage

# Function to get the memory usage of a container
def get_memory_usage(container):
    memory_usage = container.stats(stream=False)["memory_stats"]["usage"]
    return memory_usage

# Function to update the listbox
def update_listbox():
    containers = get_containers()
    listbox.delete(0, tk.END)
    for container in containers:
        listbox.insert(tk.END, container.name)

# Function to update the graph
def update_graph():
    containers = get_containers()
    for container in containers:
        if container.name == listbox.get(tk.ACTIVE):
            cpu_usage = get_cpu_usage(container)
            memory_usage = get_memory_usage(container)
            xs.append(memory_usage)
            ys.append(cpu_usage)
            line.set_xdata(xs)
            line.set_ydata(ys)
            ax.set_xlim(min(xs), max(xs))
            ax.set_ylim(min(ys), max(ys))
            canvas.draw()
    root.after(1000, update_graph)

# Function to update the listbox and graph
def update():
    update_listbox()
    update_graph()
    root.after(1000, update)

# Call the update function
update()

# Start the tkinter event loop
root.mainloop()

