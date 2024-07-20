import tkinter as tk

root = tk.Tk()

# Create a Label with text
label = tk.Label(root, text="Hello, World!", padx=20, pady=10)

# Configure the background color
label.configure(bg="lightblue")

# Pack the Label into the main window
label.pack()

root.mainloop()
