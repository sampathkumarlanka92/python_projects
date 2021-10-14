import tkinter as tk
from tkinter import ttk
# from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import font, colorchooser

root = tk.Tk()
root.title("Text Editor")
root.iconbitmap("icons/texteditor.ico")
root.geometry("1200x600")

# ---- Main menu ----
mymenu = tk.Menu()

# File Menu Drop Down
file = tk.Menu(mymenu, tearoff=False)
# file icons
newicon = tk.PhotoImage(file="icons/newfile.png")
openicon = tk.PhotoImage(file="icons/openfile.png")
saveicon = tk.PhotoImage(file="icons/savefile.png")
saveasicon = tk.PhotoImage(file="icons/saveas.png")
exiticon = tk.PhotoImage(file="icons/exit.png")
# End File Menu

# Edit Menu Drop Down
edit = tk.Menu(mymenu, tearoff=False)
# edit icons
copyicon = tk.PhotoImage(file="icons/copy.png")
cuticon = tk.PhotoImage(file="icons/cut.png")
pasteicon = tk.PhotoImage(file="icons/paste.png")
clearallicon = tk.PhotoImage(file="icons/clearall.png")
findicon = tk.PhotoImage(file="icons/find.png")

# End Edit Menu

# View Menu Drop Down
view = tk.Menu(mymenu, tearoff=False)
# view icons
toolbaricon = tk.PhotoImage(file="icons/tool.png")
statusbaricon = tk.PhotoImage(file="icons/status.png")

# End View Menu

# Colortheme Menu Drop Down
colortheme = tk.Menu(mymenu, tearoff=False)
# colortheme icons
lightredicon = tk.PhotoImage(file="icons/lightred.png")
nightblueicon = tk.PhotoImage(file="icons/nightblue.png")
defaulticon = tk.PhotoImage(file="icons/default.png")
darkicon = tk.PhotoImage(file="icons/dark.png")

# colortheme commands
themechoice = tk.StringVar()
colors = (defaulticon, lightredicon, nightblueicon, darkicon)
colors_dict = {
    "Default" : ("#000000", "#ffffff"),
    "Light Red" : ("#2d2d2d", "#ffcccb"),
    "Night Blue" : ("#ededed", "#6b9dc2"),
    "Dark" : ("#c4c4c4c", "#2d2d2d"),
}

# End Colortheme Menu

# Cascade
mymenu.add_cascade(label='File', menu=file)
mymenu.add_cascade(label='Edit', menu=edit)
mymenu.add_cascade(label='View', menu=view)
mymenu.add_cascade(label='Color Themes', menu=colortheme)
# ---- End Main Menu ----


# ---- Toolbar ----
toolbar = ttk.Label(root)
toolbar.pack(side=tk.TOP, fill=tk.X)

# Fonts
fonttuples = tk.font.families()
fontfamily = tk.StringVar()
fontbox = ttk.Combobox(toolbar, width=30, textvariable=fontfamily, state='readonly')
fontbox["values"] = fonttuples
fontbox.current(fonttuples.index('Arial'))
fontbox.grid(row=0, column=0, padx=5)

# Size
sizevar = tk.IntVar()
fontsize = ttk.Combobox(toolbar, width=14, textvariable=sizevar, state='readonly')
fontsize["values"] = tuple(range(8, 80, 2))
fontsize.current(2)
fontsize.grid(row=0, column=1, padx=5)

# bold
boldicon = tk.PhotoImage(file="icons/bold.png")
boldbtn = ttk.Button(toolbar, image=boldicon)
boldbtn.grid(row=0,column=2, padx=5)

# italic
italicicon = tk.PhotoImage(file="icons/italic.png")
italicbtn = ttk.Button(toolbar, image=italicicon)
italicbtn.grid(row=0,column=3, padx=5)

# underline
underlineicon = tk.PhotoImage(file="icons/underline.png")
underlinebtn = ttk.Button(toolbar, image=underlineicon)
underlinebtn.grid(row=0,column=4, padx=5)

# font colorchooser
colorchoosericon = tk.PhotoImage(file="icons/colorchooser.png")
colorchooserbtn = ttk.Button(toolbar, image=colorchoosericon)
colorchooserbtn.grid(row=0,column=5, padx=5)

# left align
leftalignicon = tk.PhotoImage(file="icons/leftalign.png")
leftalingbtn = ttk.Button(toolbar, image=leftalignicon)
leftalingbtn.grid(row=0,column=6, padx=5)

# justify
justifyicon = tk.PhotoImage(file="icons/justify.png")
justifybtn = ttk.Button(toolbar, image=justifyicon)
justifybtn.grid(row=0,column=7, padx=5)

# right align
rightalignicon = tk.PhotoImage(file="icons/rightalign.png")
rightalingbtn = ttk.Button(toolbar, image=rightalignicon)
rightalingbtn.grid(row=0,column=8, padx=5)

# ---- End Toolbar ----


# ---- Text Editor ----
texteditor = tk.Text(root)
texteditor.config(wrap="word", relief=tk.FLAT)

scrollbar = tk.Scrollbar(root)
texteditor.focus_set()
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
texteditor.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=texteditor.yview)
texteditor.config(yscrollcommand=scrollbar.set)

# ---- End Text Editor ----


# ---- Status Bar ----

# ---- End Status Bar ----


# ---- Main menu Functions ----
# file commands
file.add_command(label="New", image=newicon, compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label="Open", image=openicon, compound=tk.LEFT, accelerator='Ctrl+O')
file.add_command(label="Save", image=saveicon, compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label="Save As", image=saveasicon, compound=tk.LEFT, accelerator='Ctrl+Alt+S')
file.add_command(label="Exit", image=exiticon, compound=tk.LEFT, accelerator='Ctrl+Q')

# edit commands
edit.add_command(label="Copy", image=copyicon, compound=tk.LEFT, accelerator="Ctrl+C")
edit.add_command(label="Cut", image=cuticon, compound=tk.LEFT, accelerator="Ctrl+X")
edit.add_command(label="Paste", image=pasteicon, compound=tk.LEFT, accelerator="Ctrl+V")
edit.add_command(label="Clear All", image=clearallicon, compound=tk.LEFT, accelerator="Ctrl+Alt+X")
edit.add_command(label="Find", image=findicon, compound=tk.LEFT, accelerator="Ctrl+F")

# view commands
view.add_checkbutton(label="Tool Bar", image=toolbaricon, compound=tk.LEFT)
view.add_checkbutton(label="Status Bar", image=statusbaricon, compound=tk.LEFT)

# colortheme
count = 0
for color in colors_dict:
    colortheme.add_radiobutton(label=color, image=colors[count], variable=themechoice, compound=tk.LEFT)
    count += 1

# ---- End Main Menu Functions ----

root.config(menu=mymenu)
root.mainloop()
