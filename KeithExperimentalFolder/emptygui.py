from tkinter import Tk, ttk, Frame, Label, Button

# Create the main application window
root = Tk()
root.title("3D Printer GUI")
root.geometry("800x600")

# Create a Notebook (Tabbed Interface)
notebook = ttk.Notebook(root)

# Tab 1: Experiment Tab
tab1 = Frame(notebook, bg="lightgray")
notebook.add(tab1, text="Experiment")
Label(tab1, text="Start Experiment", bg="lightgray").grid(row=0, column=0, padx=10, pady=10)
Button(tab1, text="Start").grid(row=0, column=1, padx=10, pady=10)
Button(tab1, text="Stop").grid(row=0, column=2, padx=10, pady=10)

# Tab 2: Movement Tab
tab2 = Frame(notebook, bg="lightblue")
notebook.add(tab2, text="Movement")
Label(tab2, text="Move X, Y, Z", bg="lightblue").grid(row=0, column=0, padx=10, pady=10)
Button(tab2, text="X+").grid(row=1, column=1, padx=10, pady=5)
Button(tab2, text="X-").grid(row=1, column=0, padx=10, pady=5)
Button(tab2, text="Y+").grid(row=0, column=1, padx=10, pady=5)
Button(tab2, text="Y-").grid(row=2, column=1, padx=10, pady=5)
Button(tab2, text="Z+").grid(row=0, column=2, padx=10, pady=5)
Button(tab2, text="Z-").grid(row=2, column=2, padx=10, pady=5)

# Tab 3: Camera Tab
tab3 = Frame(notebook, bg="lightgreen")
notebook.add(tab3, text="Camera")
Label(tab3, text="Camera Settings", bg="lightgreen").grid(row=0, column=0, padx=10, pady=10)
Button(tab3, text="Update Settings").grid(row=1, column=0, padx=10, pady=10)

# Tab 4: Z Stack Tab
tab4 = Frame(notebook, bg="lightyellow")
notebook.add(tab4, text="Z Stack")
Label(tab4, text="Z Stack Settings", bg="lightyellow").grid(row=0, column=0, padx=10, pady=10)
Button(tab4, text="Start Z Stack").grid(row=1, column=0, padx=10, pady=10)

# Tab 5: Camera Preview Tab
tab5 = Frame(notebook, bg="lightcoral")
notebook.add(tab5, text="Preview")
Label(tab5, text="Preview Settings", bg="lightcoral").grid(row=0, column=0, padx=10, pady=10)
Button(tab5, text="Start Preview").grid(row=1, column=0, padx=10, pady=10)
Button(tab5, text="Stop Preview").grid(row=1, column=1, padx=10, pady=10)

# Tab 6: Location Helper Tab
tab6 = Frame(notebook, bg="lightpink")
notebook.add(tab6, text="Location Helper")
Label(tab6, text="Location Helper", bg="lightpink").grid(row=0, column=0, padx=10, pady=10)

# Pack the Notebook
notebook.pack(expand=True, fill="both")

# Run the application
root.mainloop()
