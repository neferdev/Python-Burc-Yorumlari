
import tkinter as tk
from tkinter import messagebox
import requests


pencere = tk.Tk()

pencere.title("Günlük Burç Yorumları")
pencere.geometry("600x600")


uygulama = tk.Frame(pencere)
uygulama.grid()


L1 = tk.Label(uygulama, text="Burcunuzu Seçiniz")
L1.grid(padx=60, pady=10)

Lb1 = tk.Listbox(uygulama)
Lb1.insert(1, "Aslan")
Lb1.insert(2, "Yengeç")
Lb1.insert(3, "Koç")
Lb1.insert(4, "Boğa")
Lb1.insert(5, "İkizler")
Lb1.insert(6, "Başak")
Lb1.insert(7, "Terazi")
Lb1.insert(8, "Akrep")
Lb1.insert(9, "Yay")
Lb1.insert(10, "Oğlak")
Lb1.insert(11, "Kova")
Lb1.insert(12, "Balık")
Lb1.grid(padx=60, pady=10)

T = tk.Text(pencere, height = 20, width = 60)
T.grid(padx=80, pady=10)
def de(event):
    Tr2Eng = str.maketrans("çğıöşü", "cgiosu")
    w = event.widget
    idx = int(w.curselection()[0])
    value = w.get(idx)
    son = value.lower().translate(Tr2Eng);
    x = requests.get('https://burc-yorumlari.herokuapp.com/get/'+son).json()
    T.insert('1.0',x[0]['GunlukYorum'])

Lb1.bind('<<ListboxSelect>>', de)



pencere.mainloop()
