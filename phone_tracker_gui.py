# phone_tracker_gui.py - A simple GUI for phone tracker.py

import tkinter as tk
import phonenumbers
from phonenumbers import geocoder, carrier

window = tk.Tk()
window.title("Phone Tracker")

lbl_title = tk.Label(text="Phone Tracker", font=("Helvetical",20))
lbl_title.pack()

lbl_number = tk.Label(text="Phone Number", font=("Arial", 12))
ent_number = tk.Entry(width=19, font=("Arial", 12))
ent_number.insert(0,"+ccxxxxxxxx")
lbl_number.pack()
ent_number.pack()

fr_btn = tk.Frame(window)
fr_btn.pack()

btn_region = tk.Button(master=fr_btn, text="Region", width=10, height=2)
btn_region.pack(side="left", expand=True)

btn_carrier = tk.Button(master=fr_btn, text="Carrier", width=10, height=2)
btn_carrier.pack(side="bottom", expand=True)

lbl_result = tk.Label(text="-", font=("Arial", 12))
lbl_result.pack()

window.mainloop()
