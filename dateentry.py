import tkinter as tk
from tkcalendar import DateEntry
root=tk.Tk()
date_label=tk.Label(root,text="Select a date:")
date_label.pack()
date_entry=DateEntry(root,width=12,background="darkblue",foreground='white',borderwidth=2)
date_entry.pack(padx=10,pady=10)
root.mainloop()