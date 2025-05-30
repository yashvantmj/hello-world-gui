import tkinter as tk

def say_hello():
    label.config(text="Hello, World!")

# Create the main window
window = tk.Tk()
window.title("Hello GUI")
window.geometry("300x150")

# Add a label
label = tk.Label(window, text="", font=("Arial", 14))
label.pack(pady=10)

# Add a button
button = tk.Button(window, text="Click Me", command=say_hello)
button.pack()

# Run the GUI event loop
window.mainloop()
