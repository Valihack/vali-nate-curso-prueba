from tkinter import *
from tkinter import ttk


def calculate (*args):
    try:
        value = float(feet.get())
        meters.set((0.3048*value*10000.0+0.5) / 10000.0 )
    except ValueError:
        pass


root = Tk()
root.title("Prueba tkinter, pies a metros")

mainframe = ttk.Frame(root, padding = "50 30 50 30")
mainframe.grid()
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable= meters).grid(column=2, row=2, sticky=W)
ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=(N, W))

ttk.Label(mainframe, text= "Pies").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text= "Es equivalente a: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text= "Metros").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()