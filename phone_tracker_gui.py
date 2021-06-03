# phone_tracker_gui.py - A simple GUI for phone tracker.py

import tkinter as tk
import phonenumbers
from phonenumbers import geocoder, carrier

window = tk.Tk()
window.title("Phone Tracker")

number_var = tk.StringVar()
def get_region():
    phone = number_var.get()
    number = phonenumbers.parse(phone)
    region = geocoder.description_for_number(number, "en")
    lbl_result["text"] = region

def get_carrier():
    phone = number_var.get()
    number = phonenumbers.parse(phone)
    carrier_phone = carrier.name_for_number(number, "en")
    lbl_result["text"] = carrier_phone

lbl_title = tk.Label(text="Phone Tracker", font=("Helvetical",20))
lbl_title.pack()

lbl_number = tk.Label(text="Phone Number", font=("Arial", 12))
ent_number = tk.Entry(width=19, font=("Arial", 12), textvariable=number_var)
ent_number.insert(0,"+ccxxxxxxxx")
lbl_number.pack()
ent_number.pack()

fr_btn = tk.Frame(window)
fr_btn.pack()

btn_region = tk.Button(master=fr_btn, text="Region", width=10, height=2, command=get_region)
btn_region.pack(side="left", expand=True)

btn_carrier = tk.Button(master=fr_btn, text="Carrier", width=10, height=2, command=get_carrier)
btn_carrier.pack(side="bottom", expand=True)

lbl_result = tk.Label(text="-", font=("Arial", 12))
lbl_result.pack()

window.mainloop()
