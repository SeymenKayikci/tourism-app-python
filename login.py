import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import subprocess

win = Tk()
win.geometry("340x440")
win.title("Giriş Paneli")
win.config(bg="#333333")

def kayit_ol():
    messagebox.showinfo("Geri Dönülüyor", "Kayıt Ekranına Yönlendirildiniz")
    subprocess.run(["python", "kayit.py"])

def login():
    username = username_entry.get()
    password = password_entry.get()

    try:
        # MySQL bağlantı ayarları
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'root',
            'database': 'giris',  # Oluşturduğunuz veritabanı adı
            'port': 8889
        }
        # MySQL bağlantısı oluştur
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Kullanıcı adı ve şifreyi kontrol et
        query = "SELECT * FROM kayit WHERE kullanici_adi = %s AND sifre = %s"
        user_data = (username, password)
        cursor.execute(query, user_data)
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Başarılı", "Başarıyla giriş yaptınız.")
            subprocess.run(["python", "secenek.py"])
        else:
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı.")

    except mysql.connector.Error as err:
        # Hata durumunda
        messagebox.showerror("Hata", "Giriş yapma sırasında bir hata oluştu: {}".format(err))

    finally:
        # Bağlantıyı kapat
        if conn.is_connected():
            cursor.close()
            conn.close()

notebook = ttk.Notebook(win)
frame = tkinter.Frame(bg="#333333")

login_label = Label(frame, text="Turizm ", bg="#333333", fg="blue", font=("arial", 30))
username_label = Label(frame, text="Kullanıcı Adı", bg="#333333", fg="#FFFFFF", font=("arial", 16))
username_entry = Entry(frame, font=("arial", 16))
password_entry = Entry(frame, show="*", font=("arial", 16))
password_label = Label(frame, text="Şifre", bg="#333333", fg="#FFFFFF", font=("arial", 16))
login_button = Button(frame, text="Giriş", fg="blue", font=("arial", 16), command=login)
kayit_button = Button(frame, text="Kayıt Ol", fg="blue", font=("arial", 16), command=kayit_ol)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
kayit_button.grid(row=4, column=0, columnspan=2)

frame.pack()
win.mainloop()
