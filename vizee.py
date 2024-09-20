import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import subprocess


def geri_don():
    messagebox.showinfo("Geri Dönülüyor","Seçenek Sayfasına Yönlendirildiniz")
    subprocess.run(["python", "secenek.py"])
def submit_form():
    ad = ad_entry.get()
    soyad = soyad_entry.get()
    dogum_tarihi = dogum_tarihi_entry.get()
    cinsiyet = cinsiyet_var.get()
    medeni_hal = medeni_hal_var.get()

    if not ad or not soyad or not dogum_tarihi or not cinsiyet or not medeni_hal:
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
            insert_query = "INSERT INTO vize(ad, soyad, dogum_tarihi , cinsiyet, medeni_hal) VALUES (%s, %s, %s, %s, %s)"
            user_data = (ad, soyad, dogum_tarihi, cinsiyet,medeni_hal)
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
    print("Ad:", ad)
    print("Soyad:", soyad)
    print("Doğum Tarihi:", dogum_tarihi)
    print("Cinsiyet:", cinsiyet)
    print("Medeni Hal:", medeni_hal)

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Vize Başvuru Formu")

# Etiketler ve giriş kutuları
ad_label = ttk.Label(root, text="Ad:")
ad_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
ad_entry = ttk.Entry(root)
ad_entry.grid(row=0, column=1, padx=10, pady=5)

soyad_label = ttk.Label(root, text="Soyad:")
soyad_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
soyad_entry = ttk.Entry(root)
soyad_entry.grid(row=1, column=1, padx=10, pady=5)

dogum_tarihi_label = ttk.Label(root, text="Doğum Tarihi:")
dogum_tarihi_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
dogum_tarihi_entry = ttk.Entry(root)
dogum_tarihi_entry.grid(row=2, column=1, padx=10, pady=5)

cinsiyet_label = ttk.Label(root, text="Cinsiyet:")
cinsiyet_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
cinsiyet_var = tk.StringVar()
cinsiyet_combobox = ttk.Combobox(root, textvariable=cinsiyet_var, values=["Erkek", "Kadın", "Diğer"])
cinsiyet_combobox.grid(row=3, column=1, padx=10, pady=5)

medeni_hal_label = ttk.Label(root, text="Medeni Hal:")
medeni_hal_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
medeni_hal_var = tk.StringVar()
medeni_hal_combobox = ttk.Combobox(root, textvariable=medeni_hal_var, values=["Bekar", "Evli", "Boşanmış"])
medeni_hal_combobox.grid(row=4, column=1, padx=10, pady=5)

geri_don_button=ttk.Button(root,text="Geri Dön",command=geri_don)
geri_don_button.grid(row=6,column=0,columnspan=2,pady=10)

# Gönderme düğmesi
submit_button = ttk.Button(root, text="Formu Gönder", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Ana döngüyü başlat
root.mainloop()
