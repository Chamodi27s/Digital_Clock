import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Clock")

# Create label first
label = tk.Label(root, font=('calibri', 50, 'bold'),
                 background='yellow', foreground='black')
label.pack(anchor='center')

# Define update function
def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, time)

# Start the clock
time()
root.mainloop()
