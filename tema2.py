import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

x = 7
y = 13
print(f'x = {x}, y = {y}')

plt.style.use('dark_background')

file_path = 'data.csv'
data = pd.read_csv(file_path)

root = tk.Tk()
root.title("Tema 2")

canvas_frame = ttk.Frame(root)
canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

canvas = tk.Canvas(canvas_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

fig_all, ax_all = plt.subplots()
data.plot(ax=ax_all, title='Toate valorile')
ax_all.text(0.95, 0.95, 'Olteanu Rares-Cristian', transform=ax_all.transAxes, color='red', fontsize=12,
            ha='right', va='top')
canvas_all = FigureCanvasTkAgg(fig_all, master=frame)
canvas_all.draw()
canvas_all.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

fig_head, ax_head = plt.subplots()
data.head(x).plot(ax=ax_head, title=f'Primele {x} valori')
ax_head.text(0.95, 0.95, 'Olteanu Rares-Cristian', transform=ax_head.transAxes, color='red', fontsize=12,
             ha='right', va='top')
canvas_head = FigureCanvasTkAgg(fig_head, master=frame)
canvas_head.draw()
canvas_head.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

fig_tail, ax_tail = plt.subplots()
data[['Durata', 'Puls']].tail(y).plot(ax=ax_tail, title=f'Ultimele {y} valori pentru Durata si Puls')
ax_tail.text(0.95, 0.95, 'Olteanu Rares-Cristian', transform=ax_tail.transAxes, color='red', fontsize=12,
             ha='right', va='top')
canvas_tail = FigureCanvasTkAgg(fig_tail, master=frame)
canvas_tail.draw()
canvas_tail.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * int(event.delta / 120), "units"))

root.geometry(f"{int(frame.winfo_reqwidth())}x{int(frame.winfo_reqheight())}")

root.mainloop()
