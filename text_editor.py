import tkinter as tk
from tkinter import ttk
# from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import font, colorchooser
import os

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
    "Dark" : ("#c4c4c4", "#2d2d2d"),
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

# fontfamily and fontsize functionas
cur_fontfam = 'Arial'
cur_fontsize = 12

def changefont(event=None):
    global cur_fontfam
    cur_fontfam = fontfamily.get()
    texteditor.configure(font=(cur_fontfam, cur_fontsize))

def changefontsize(event=None):
    global cur_fontsize
    cur_fontsize = sizevar.get()
    texteditor.configure(font=(cur_fontfam, cur_fontsize))


fontbox.bind("<<ComboboxSelected>>", changefont)
fontsize.bind("<<ComboboxSelected>>", changefontsize)

# buttons functions
# bold button functionality
def changebold():
    textproperty = tk.font.Font(font=texteditor['font'])
    if textproperty.actual()['weight'] == 'normal':
        texteditor.configure(font=(cur_fontfam, cur_fontsize, 'bold'))
    if textproperty.actual()['weight'] == 'bold':
        texteditor.configure(font=(cur_fontfam, cur_fontsize, 'normal'))

boldbtn.configure(command=changebold)

# italic functionlaity
def changeitalic():
    textproperty = tk.font.Font(font=texteditor['font'])
    if textproperty.actual()['slant'] == 'roman':
        texteditor.configure(font=(cur_fontfam, cur_fontsize, 'italic'))
    if textproperty.actual()['slant'] == 'italic':
        texteditor.configure(font=(cur_fontfam, cur_fontsize, 'normal'))

italicbtn.configure(command=changeitalic)

# underline functionality
def changeunderline():
    textproperty = tk.font.Font(font=texteditor['font'])
    if textproperty.actual()['underline'] == 0:
        texteditor.configure(font=(cur_fontfam, cur_fontsize, 'underline'))
    if textproperty.actual()['underline'] == 1:
        texteditor.configure(font=(cur_fontfam, cur_fontsize, 'normal'))

underlinebtn.configure(command=changeunderline)

## font color functionality
def changefontcolor():
    colorvar = tk.colorchooser.askcolor()
    texteditor.configure(fg=colorvar[1])


colorchooserbtn.configure(command=changefontcolor)

### align functionality

def alignleft():
    textcontent = texteditor.get(1.0, 'end')
    texteditor.tag_config('left', justify=tk.LEFT)
    texteditor.delete(1.0, tk.END)
    texteditor.insert(tk.INSERT, textcontent, 'left')

leftalingbtn.configure(command=alignleft)

## center
def aligncenter():
    textcontent = texteditor.get(1.0, 'end')
    texteditor.tag_config('center', justify=tk.CENTER)
    texteditor.delete(1.0, tk.END)
    texteditor.insert(tk.INSERT, textcontent, 'center')

justifybtn.configure(command=aligncenter)

## right
def alignright():
    textcontent = texteditor.get(1.0, 'end')
    texteditor.tag_config('right', justify=tk.RIGHT)
    texteditor.delete(1.0, tk.END)
    texteditor.insert(tk.INSERT, textcontent, 'right')

rightalingbtn.configure(command=alignright)

texteditor.configure(font=('Arial', 12))

# ---- End Text Editor ----


# ---- Status Bar ----
statusbar = ttk.Label(root, text='Status Bar')
statusbar.pack(side=tk.BOTTOM)

textchanged = False
def changed(event=None):
    global textchanged
    if texteditor.edit_modified():
        textchanged = True
        words = len(texteditor.get(1.0, 'end-1c').split())
        characters = len(texteditor.get(1.0, 'end-1c'))
        statusbar.config(text=f'Characters : {characters} Words : {words}')
    texteditor.edit_modified(False)

texteditor.bind('<<Modified>>', changed)

# ---- End Status Bar ----


# ---- Main menu Functions ----
## variable
url = ''

# file commands
## new functionality
def newfile(event=None):
    global url
    url = ''
    texteditor.delete(1.0, tk.END)

file.add_command(label="New", image=newicon, compound=tk.LEFT, accelerator='Ctrl+N', command=newfile)

## open functionality

def openfile(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            texteditor.delete(1.0, tk.END)
            texteditor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    root.title(os.path.basename(url))

file.add_command(label="Open", image=openicon, compound=tk.LEFT, accelerator='Ctrl+O', command=openfile)

## save file

def savefile(event=None):
    global url
    try:
        if url:
            content = str(texteditor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = texteditor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return

file.add_command(label="Save", image=saveicon, compound=tk.LEFT, accelerator='Ctrl+S', command=savefile)

## save as functionality
def saveas(event=None):
    global url
    try:
        content = texteditor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return

file.add_command(label="Save As", image=saveasicon, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=saveas)

## exit functionality

def exitfunc(event=None):
    global url, textchanged
    try:
        if textchanged:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = texteditor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        root.destroy()
                else:
                    content2 = str(texteditor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return

file.add_command(label="Exit", image=exiticon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exitfunc)


############ find functionality

def findfunc(event=None):

    def find():
        word = findinput.get()
        texteditor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            startpos = '1.0'
            while True:
                startpos = texteditor.search(word, startpos, stopindex=tk.END)
                if not startpos:
                    break
                endpos = f'{startpos}+{len(word)}c'
                texteditor.tag_add('match', startpos, endpos)
                matches += 1
                startpos = endpos
                texteditor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = findinput.get()
        replacetext = replaceinput.get()
        content = texteditor.get(1.0, tk.END)
        newcontent = content.replace(word, replacetext)
        texteditor.delete(1.0, tk.END)
        texteditor.insert(1.0, newcontent)

    finddialogue = tk.Toplevel()
    finddialogue.geometry('450x250+500+200')
    finddialogue.title('Find')
    finddialogue.resizable(0,0)

    ## frame
    findframe = ttk.LabelFrame(finddialogue, text='Find/Replace')
    findframe.pack(pady=20)

    ## labels
    textfindlabel = ttk.Label(findframe, text='Find : ')
    textreplacelabel = ttk.Label(findframe, text= 'Replace')

    ## entry
    findinput = ttk.Entry(findframe, width=30)
    replaceinput = ttk.Entry(findframe, width=30)

    ## button
    findbutton = ttk.Button(findframe, text='Find', command=find)
    replacebutton = ttk.Button(findframe, text= 'Replace', command=replace)

    ## label grid
    textfindlabel.grid(row=0, column=0, padx=4, pady=4)
    textreplacelabel.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid
    findinput.grid(row=0, column=1, padx=4, pady=4)
    replaceinput.grid(row=1, column=1, padx=4, pady=4)

    ## button grid
    findbutton.grid(row=2, column=0, padx=8, pady=4)
    replacebutton.grid(row=2, column=1, padx=8, pady=4)

    finddialogue.mainloop()


# edit commands
edit.add_command(label="Copy", image=copyicon, compound=tk.LEFT, accelerator="Ctrl+C", command=lambda:texteditor.event_generate("<Control c>"))
edit.add_command(label="Cut", image=cuticon, compound=tk.LEFT, accelerator="Ctrl+X", command=lambda:texteditor.event_generate("<Control x>"))
edit.add_command(label="Paste", image=pasteicon, compound=tk.LEFT, accelerator="Ctrl+V", command=lambda:texteditor.event_generate("<Control v>"))
edit.add_command(label="Clear All", image=clearallicon, compound=tk.LEFT, accelerator="Ctrl+Alt+X", command= lambda:texteditor.delete(1.0, tk.END))
edit.add_command(label="Find", image=findicon, compound=tk.LEFT, accelerator="Ctrl+F", command = findfunc)


## view check button

showstatusbar = tk.BooleanVar()
showstatusbar.set(True)
showtoolbar = tk.BooleanVar()
showtoolbar.set(True)

def hidetoolbar():
    global showtoolbar
    if showtoolbar:
        toolbar.pack_forget()
        showtoolbar = False
    else :
        texteditor.pack_forget()
        statusbar.pack_forget()
        toolbar.pack(side=tk.TOP, fill=tk.X)
        texteditor.pack(fill=tk.BOTH, expand=True)
        statusbar.pack(side=tk.BOTTOM)
        showtoolbar = True


def hidestatusbar():
    global showstatusbar
    if showstatusbar:
        statusbar.pack_forget()
        showstatusbar = False
    else :
        statusbar.pack(side=tk.BOTTOM)
        showstatusbar = True


# view commands
view.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=0, variable = showtoolbar, image=toolbaricon, compound=tk.LEFT, command=hidetoolbar)
view.add_checkbutton(label="Status Bar", onvalue=1, offvalue=False, variable = showstatusbar, image=statusbaricon, compound=tk.LEFT, command=hidestatusbar)

# colortheme
## color theme
def changetheme():
    chosentheme = themechoice.get()
    colortuple = colors_dict.get(chosentheme)
    fgcolor, bgcolor = colortuple[0], colortuple[1]
    texteditor.config(background=bgcolor, fg=fgcolor)

count = 0
for color in colors_dict:
    colortheme.add_radiobutton(label=color, image=colors[count], variable=themechoice, compound=tk.LEFT, command=changetheme)
    count += 1

# ---- End Main Menu Functions ----

root.config(menu=mymenu)
## bind shortcut keys
root.bind("<Control-n>", newfile)
root.bind("<Control-o>", openfile)
root.bind("<Control-s>", savefile)
root.bind("<Control-Alt-s>", saveas)
root.bind("<Control-q>", exitfunc)
root.bind("<Control-f>", findfunc)

root.mainloop()
