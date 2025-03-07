
# tkinter application with embeded matplot graphs

#imports
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np 

# Create a Tkinter window
root = tk.Tk()
root.title("Black Sholes Model Plotter")

# Sample data for the plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(6, 4))  # You can adjust the size of the chart
ax.plot(x, y, label="Sine Wave")
ax.set_title("Price till Expiration")
ax.set_xlabel("Days till Expiration")
ax.set_ylabel("Price of Option")
ax.legend()

# Embed the plot in the Tkinter window using a Canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# Entry widgets for user input
side_frame = tk.Frame(root)
side_frame.grid(row=1,column=2)

label_price = tk.Label(side_frame, text="Option Price").grid(row=0,column=0)
entry_price = tk.Entry(side_frame, width=20).grid(row=1,column=0)
label_stirke = tk.Label(side_frame, text="Strike Price").grid(row=2,column=0)
entry_stirke = tk.Entry(side_frame, width=20).grid(row=3,column=0)
label_Ex = tk.Label(side_frame, text="Days till Exp.").grid(row=4,column=0)
entry_Ex = tk.Entry(side_frame, width=20).grid(row=5,column=0)

# Create a Tkinter canvas and pack it into the window
canvas.get_tk_widget().grid(row=1,column=0)

#closing Program
# Add a quit button
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.grid(row=0,column=2)
root.protocol("WM_DELETE_WINDOW", root.quit) #bind x on window to close program

# Run the Tkinter main loop
root.mainloop()