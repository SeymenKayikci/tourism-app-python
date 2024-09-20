import tkinter as tk
from tkinter import messagebox
import mysql.connector

def kayit_ol():
    ad = entry_ad.get()
    soyad = entry_soyad.get()
    kullanici_adi = entry_kullanici_adi.get()
    sifre = entry_sifre.get()

    if not ad or not soyad or not kullanici_adi or not sifre:
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
            insert_query = "INSERT INTO kayit(ad, soyad, kullanici_adi, sifre) VALUES (%s, %s, %s, %s)"
            user_data = (ad, soyad, kullanici_adi, sifre)
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

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Kayıt Ekranı")

# Etiketler ve giriş alanları
label_ad = tk.Label(root, text="Ad:")
label_ad.grid(row=0, column=0, padx=10, pady=10)
entry_ad = tk.Entry(root)
entry_ad.grid(row=0, column=1, padx=10, pady=10)

label_soyad = tk.Label(root, text="Soyad:")
label_soyad.grid(row=1, column=0, padx=10, pady=10)
entry_soyad = tk.Entry(root)
entry_soyad.grid(row=1, column=1, padx=10, pady=10)

label_kullanici_adi = tk.Label(root, text="Kullanıcı Adı:")
label_kullanici_adi.grid(row=2, column=0, padx=10, pady=10)
entry_kullanici_adi = tk.Entry(root)
entry_kullanici_adi.grid(row=2, column=1, padx=10, pady=10)

label_sifre = tk.Label(root, text="Şifre:")
label_sifre.grid(row=3, column=0, padx=10, pady=10)
entry_sifre = tk.Entry(root, show="*")
entry_sifre.grid(row=3, column=1, padx=10, pady=10)

# Kayıt olma butonu
btn_kayit_ol = tk.Button(root, text="Kayıt Ol", command=kayit_ol)
btn_kayit_ol.grid(row=4, column=0, columnspan=2, pady=10)

# Pencereyi başlat
root.mainloop()
