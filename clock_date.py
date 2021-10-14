import tkinter as tk
from tkinter import ttk
from time import strftime
from datetime import datetime
import pytz

root = tk.Tk()
root.title("Clock")
root.resizable(0, 0)

ist = pytz.timezone("Asia/Kolkata")

def date_time():
    t = datetime.now(ist)
    # time
    tm = t.strftime("%I:%M:%S %p")
    # date
    d = t.strftime("%d %b %Y")

    timelabel.config(text=tm)
    datelabel.config(text=d)
    timelabel.after(1000, date_time)

timelabel = tk.Label(root, font=("ds-digital", 80), bg="lightblue", fg="orange")
timelabel.pack(anchor="center")

datelabel = tk.Label(root, font=("ds-digital", 80), bg="lightblue", fg="orange")
datelabel.pack(fill=tk.BOTH, anchor="center")

date_time()

root.mainloop()
