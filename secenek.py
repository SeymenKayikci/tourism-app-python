import tkinter as tk
from tkinter import messagebox
import subprocess

def open_vize_page():
    messagebox.showinfo("Vize Sayfası", "Vize sayfasına yönlendirildiniz.")
    subprocess.run(["python", "vizee.py"])

def open_pasaport_page():
    messagebox.showinfo("Pasaport Sayfası", "Pasaport sayfasına yönlendirildiniz.")
    subprocess.run(["python", "pasaport.py"])

def open_ucak_bileti_page():
    messagebox.showinfo("Uçak Bileti Sayfası", "Uçak bileti sayfasına yönlendirildiniz.")
    subprocess.run(["python", "ucak_bileti.py"])

win = tk.Tk()
win.title("Seçim Ekranı")
win.geometry("300x300")
win.config(bg="#333333")

frame = tk.Frame(win, bg="#333333")

vize_button = tk.Button(frame, text="Vize", fg="blue", font=("arial", 16), command=open_vize_page)
pasaport_button = tk.Button(frame, text="Pasaport", fg="blue", font=("arial", 16), command=open_pasaport_page)
ucak_bileti_button = tk.Button(frame, text="Uçak Bileti", fg="blue", font=("arial", 16), command=open_ucak_bileti_page)


vize_button.grid(row=0, column=0, pady=20, padx=100)
pasaport_button.grid(row=1, column=0, pady=20, padx=100)
ucak_bileti_button.grid(row=2, column=0, pady=20, padx=100)

frame.pack()
win.mainloop()
