import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

meyve_klasoru = "meyveler/"
meyve_adlari = []


for meyve_ad in os.listdir(meyve_klasoru):
    if meyve_ad.endswith(".jpg"):
        meyve_adlari.append(meyve_ad[:-4])

def resim_sec():

    dosya_yolu = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg")])
    resim_yukle(dosya_yolu)

def resim_yukle(dosya_yolu):
    # Seçilen resmi yüklüyoruz, boyutlandırıyoruz ve RGBA formatına dönüştürüyoruz
    resim = Image.open(dosya_yolu)
    resim = resim.resize((150, 150))
    resim = resim.convert("RGBA")

    img = ImageTk.PhotoImage(resim)
#armur
    # Yüklenen resmi etikete yerleştiriyoruz
    yuklenen_resim_label.configure(image=img)
    yuklenen_resim_label.image = img

    # İşlenmiş resmi bulmak için isle_resim fonksiyonunu çağırıyoruz
    sonuc = isle_resim(dosya_yolu)
    sonuc_label.configure(text=f"Eşleşen Resim adı: {sonuc}")
    abc_label.configure(text=f"Eşleşen Meyve: {sonuc[:-2]}")

def isle_resim(dosya_yolu):  # Resmi yüklüyoruz RGBA kırmızı yeşil mavi alfa (saydam)  formatına dönüştürüyoruz
    resim = Image.open(dosya_yolu)
    resim = resim.resize((150, 150))
    resim = resim.convert("RGBA")
    piksel_degerleri = list(resim.getdata())

    # Her bir meyve adı için işleme yapılıyor
    for meyve_ad in meyve_adlari:
        meyve_resim_yolu = os.path.join(meyve_klasoru, meyve_ad + ".jpg")
        meyve_resim = Image.open(meyve_resim_yolu)
        meyve_resim = meyve_resim.resize((150, 150))
        meyve_resim = meyve_resim.convert("RGBA")
        meyve_piksel_degerleri = list(meyve_resim.getdata())

        if piksel_degerleri == meyve_piksel_degerleri: #if 1 olursa meyve eşleşir döngü biter meyve adı yazdırılır
            return meyve_ad

    return "Meyve Bulunamadı"


pencere = tk.Tk()
pencere.title("Görüntü İşleme Final Ödevi")
pencere.configure(bg="Light Cyan")
pencere.geometry("600x550")
ikon_resim = Image.open("ucak.png")
pencere.iconphoto(True, ImageTk.PhotoImage(ikon_resim))


resim_ekle_button = tk.Button(pencere, text="Resim Ekle", command=resim_sec)
resim_ekle_button.pack(pady=(60, 20))

isim_label = tk.Label(pencere, text="Doç.Dr.Erdinç KOÇER\nSerkan Tuğrul ARTUT\nNO: 203302039", bg="Light Cyan")
isim_label.pack(side=tk.BOTTOM, anchor=tk.SE, pady=10, padx=10)

yuklenen_resim_label = tk.Label(pencere, bg="Light Cyan")
yuklenen_resim_label.pack(pady=20)

sonuc_label = tk.Label(pencere, text="", bg="Light Cyan")
sonuc_label.pack(pady=20)

abc_label = tk.Label(pencere, text="", bg="Light Cyan")
abc_label.pack(pady=15)

pencere.mainloop()
