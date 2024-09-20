import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import subprocess

def geri_don():
    messagebox.showinfo("Geri Dönülüyor","Seçenek Sayfasına Yönlendirildiniz")
    subprocess.run(["python", "secenek.py"])

def find_ticket():
    nereden = nereden_combobox.get()
    nereye = nereye_combobox.get()
    gidis_tarihi = gidis_tarihi_entry.get()
    donus_tarihi = donus_tarihi_entry.get()
    yolcu_sayisi = yolcu_sayisi_spinbox.get()

    if not nereden or not nereye or not gidis_tarihi or not donus_tarihi or not yolcu_sayisi:
        messagebox.showerror("Hata", "Tüm alanları doldurmalısınız.")
    else:
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

            # Kullanıcı bilgilerini tabloya ekleyin
            insert_query = "INSERT INTO ucak_bileti(nereden, nereye, gidis_tarihi , donus_tarihi, yolcu_sayisi) VALUES (%s, %s, %s, %s, %s)"
            user_data = (nereden, nereye, gidis_tarihi, donus_tarihi, yolcu_sayisi)
            cursor.execute(insert_query, user_data)

            # Veritabanına yapılan değişiklikleri kaydet
            conn.commit()

            # Başarı mesajı
            messagebox.showinfo("Başarılı", "Kayıt başarıyla oluşturuldu.")

        except mysql.connector.Error as err:
            # Hata durumunda
            messagebox.showerror("Hata", "Kayıt olma sırasında bir hata oluştu: {}".format(err))

        finally:
            # Bağlantıyı kapat
            if conn.is_connected():
                cursor.close()
                conn.close()

    # Verileri kullanarak istediğiniz işlemleri yapabilirsiniz
    print("Nereden:", nereden)
    print("Nereye:", nereye)
    print("Gidiş Tarihi:", gidis_tarihi)
    print("Dönüş Tarihi:", donus_tarihi)
    print("Yolcu Sayısı:", yolcu_sayisi)

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Uçak Bilet Sayfası")

# Etiketler ve giriş kutuları
nereden_label = ttk.Label(root, text="Nereden:")
nereden_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
nereden_combobox = ttk.Combobox(root, values=["İstanbul", "Ankara", "İzmir", "Antalya"])
nereden_combobox.grid(row=0, column=1, padx=10, pady=5)

nereye_label = ttk.Label(root, text="Nereye:")
nereye_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
nereye_combobox = ttk.Combobox(root, values=["New York", "Paris", "Tokyo", "Dubai"])
nereye_combobox.grid(row=1, column=1, padx=10, pady=5)

gidis_tarihi_label = ttk.Label(root, text="Gidiş Tarihi:")
gidis_tarihi_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
gidis_tarihi_entry = ttk.Entry(root)
gidis_tarihi_entry.grid(row=2, column=1, padx=10, pady=5)

donus_tarihi_label = ttk.Label(root, text="Dönüş Tarihi:")
donus_tarihi_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
donus_tarihi_entry = ttk.Entry(root)
donus_tarihi_entry.grid(row=3, column=1, padx=10, pady=5)

yolcu_sayisi_label = ttk.Label(root, text="Yolcu Sayısı:")
yolcu_sayisi_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
yolcu_sayisi_spinbox = ttk.Spinbox(root, from_=1, to=10)
yolcu_sayisi_spinbox.grid(row=4, column=1, padx=10, pady=5)

geri_don_button=ttk.Button(root,text="Geri Dön",command=geri_don)
geri_don_button.grid(row=6,column=0,columnspan=2,pady=10)

# Bilet Bul butonu
find_ticket_button = ttk.Button(root, text="Bilet Bul", command=find_ticket)
find_ticket_button.grid(row=5, column=0, columnspan=2, pady=10)

# Ana döngüyü başlat
root.mainloop()
