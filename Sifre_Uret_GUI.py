# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import END, messagebox
import random

sozluk = {
        "A" : ["@", "4", "æ", "^", "₳", "∆", "ᴁ", "Д", "Ʌ", "∂"],
        "B" : ["8", "β", "ß", "Þ", ">", "%", ":", "∞", "lo", "1o", "|o", "₿", "Ƃ"],
        "C" : ["(", "©", "{", "¿", "<", "[", "Ȼ", "ȼ", "ᴐ", "Ɔ"],
        "Ç" : [".(", "¢", "©.", "{.", "¿.", ".<", ".[", ".ɶ", "ᴐ." ],
        "D" : ["|)", "o|", "o1", "ol", "}", "Þ", ">", "]"],
        "E" : ["3", "€", "æ", "ɘ", "Ȼ", "ȼ", "∑"],
        "F" : ["ⅎ", "╒", "Ŧ", "ʃ"],
        "G" : ["@", "¿", "₲", "6", "9", "ɠ", "∂"],
        "Ğ" : ["₲", "¿", "6", "9", "ɠ"],
        "H" : ["|-|", "|n", "1n", "ln", "Ĥ", "Ħ", "ħ"],
        "I" : ["|", "_", "1", "l"],
        "İ" : ["|.", "¡", "¦", "!", "-.", "_.", "1.", "l."],
        "J" : ["]", "Ĳ", "ĳ", "ǰ", "ɟ", "˩", "ʃ", "˩", "⌡", "╝"],
        "K" : ["|<", "l<", "1<", "Ӄ","ӂ","Ӝ"],
        "L" : ["£", "|", "|_", "1", "7"],
        "M" : ["µ", "π", "|\/|", "l\/l", "1\/1", "w", "W"],
        "N" : ["Ω", "π", "∏", "Л", "η", "|\|", "l\l", "I\I", "1\1", "И"],
        "O" : ["Ø", "ø", "ᴓ", "0"],
        "Ö" : ["Ø..", "ø..", "ᴓ..", ".Ø.", ".ø.", ".ᴓ.", "0..", ".0.", ".o.", ".O."],
        "P" : ["|º", "lº", "1º", "¶", "℗"],
        "Q" : ["Ø", "φ"],
        "R" : ["®", "┌", "ı", "Ӷ"],
        "S" : ["5", "&", "§", "~", "∫", "≈", "δ"],
        "Ş" : ["$", ".&", "§", "~.", ".δ", "5."],
        "T" : ["ŧ", "Ł", "ł", "ǂ", "┬", "Ԏ", "7","-|-"],
        "U" : ["Ʊ", "ᴗ", "|_|", "l_l", "1_1"],
        "Ü" : ["Ʊ..", "ᴗ..", "U..", "u..", ".u.", ".U.", ".|_|.", ".l_l.", ".1_1."],
        "V" : ["√", "\/", "Ɣ","˅"],
        "W" : ["ῶ", "ψ", "ᴪ", "Ш"],
        "X" : ["*", "#", "ӂ", "Ӝ"],
        "Y" : ["¥", "ψ", "ᴪ", "λ", "ʮ"],
        "Z" : ["≠", "2", "|\|", "1\1"],
        " " : [" ", "_", "-", ".", ","]
        }

#Fonksiyonlar

def sifre_uret():
        
    alfabe = "abcçdefgğhıijklmnoöpqrsştuüvwxyz ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ"

    for karakter in girdi.get():
        if karakter not in alfabe:
            messagebox.showerror("Hatalı Karakter!","İzin verilen karakterlerin dışında bir veya daha fazla karakter yazdığınız için, işleme devam edilemiyor!\nKullanılabilir karakterler şunlardır:\nabcçdefgğhıijklmnoöpqrsştuüvwxyz")
            break
        
        else:
            sifrelenen = ""
            for harf in girdi.get().upper():               
                sifrelenen += random.choice(sozluk[harf])
            sonuc_penceresi.insert(END,sifrelenen + "\n")

            uretilen_sifre_miktari = int(sonuc_penceresi.index("end")[:-2]) - 2
            if uretilen_sifre_miktari > 0:
                btn_kaydet.configure(state = "normal")

            break

def kaydet():
    sonuc = int(sonuc_penceresi.index("end")[:-2]) - 2
    if sonuc > 0:
        with open("Şifreli_Metin.txt", "w", encoding="UTF-8") as dosya:
            bulunan_kelime = str(int(sonuc_penceresi.index("end")[:-2]) - 2)
            dosya.write("'" + girdi.get() + "' Kelimesi için " + bulunan_kelime + " adet şifre üretilmiştir .\nÜretilen Şifreli kelimeler, aşağıda listelenmiştir.\n\n" + sonuc_penceresi.get("1.0","end"))
    else:
        messagebox.showinfo("Kaydedilecek Veri Yok!","Arama işlemi başlatılmadığı ya da arama sonucunda kelime bulunamadığı için, kayıt işlemi gerçekleştirilemiyor.")


def temizle():
    girdi.delete(0, tk.END)
    sonuc_penceresi.delete("1.0",tk.END)
    btn_kaydet.configure(state = "disabled")

def pencere_hakkinda():     # "Hakkında" Penceresinin Özellikleri ve Metni                      
    hakkinda = tk.Toplevel()
    hakkinda.title("Hakkında")
    hakkinda.geometry("300x125")
    hakkinda.resizable("FALSE", "FALSE")
    bilgi = tk.Label(hakkinda, text="\nŞifre Üret\n\nKodlayan: Mustafa Halil\n\nhttps://github.com/mhalil\n")
    bilgi.pack()

    
# Pencere Ebatları ve Renk Tanımları
arkaplan_rengi = "#5dade2"
arkaplan_rengi_metin = "#aed6f1"
arkaplan_rengi_buton = "#2980b9"

pencere = tk.Tk()
pencere.geometry("300x465+600+300")
pencere.resizable("FALSE", "FALSE")
pencere.title(".:: ŞİFRE ÜRET ::.")
pencere.configure(bg = arkaplan_rengi)

# Arayüz Unsurlarının (Widget) Yerleşimi

menu_cubugu = tk.Menu(pencere, activebackground="#5dade2",activeforeground="white")
pencere.config(menu=menu_cubugu) #menümüzü oluşturduk

dosya_menusu = tk.Menu(menu_cubugu)
menu_cubugu.add_cascade(label="Dosya", menu=dosya_menusu)
dosya_menusu.add_command(label="Şifre Üret", command=sifre_uret)
dosya_menusu.add_command(label="Temizle", command=temizle)
dosya_menusu.add_command(label="Kaydet", command=kaydet)
dosya_menusu.add_command(label="Kapat", command=pencere.quit, accelerator= "Ctrl+Q")

pencere.bind("<Control-q>", exit)
pencere.bind("<Control-Q>", exit)

hakkinda_menusu = tk.Menu(menu_cubugu, tearoff=0)
menu_cubugu.add_cascade(label="Hakkında", menu=hakkinda_menusu)
hakkinda_menusu.add_command(label="Hakkında", command=pencere_hakkinda)   

aciklama = tk.Label(pencere, text = "Şifrelemek istediğiniz metni \naşağıdaki kutuya yazın.",
                    fg = "white",
                    bg = arkaplan_rengi,
                    font = "Verdana,Tahoma,DejaVuSans,LiberationSans,Ubuntu 11 bold")
aciklama.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

girdi = tk.Entry(pencere, 
                width=34,
                bg = arkaplan_rengi_metin)
girdi.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

sonuc_penceresi = tk.Text(pencere,
                width=34,
                height=14,
                font = "Tahoma,Verdana,DejaVuSans,LiberationSans,Ubuntu 10",
                state="normal",
                bg = arkaplan_rengi_metin)
sonuc_penceresi.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

btn_genisligi = 12

btn_sifre_uret = tk.Button(pencere,
                    text = "Şifre Üret",
                    width = btn_genisligi,
                    height=2,
                    font = "Verdana,Tahoma,DejaVuSans,LiberationSans,Ubuntu 10 bold",
                    bg = arkaplan_rengi_buton,
                    fg = "white",
                    command= sifre_uret)
btn_sifre_uret.grid(row=3, column=0, padx=5, pady=5)

btn_temizle = tk.Button(pencere,
                    text = "Temizle",
                    width = btn_genisligi,
                    height=2,
                    font = "Verdana,Tahoma,DejaVuSans,LiberationSans,Ubuntu 10 bold",
                    bg = arkaplan_rengi_buton,
                    fg = "white",
                    command= temizle)
btn_temizle.grid(row=3, column=1, padx=5, pady=5)


btn_kaydet = tk.Button(pencere,
                    text = "Kaydet",
                    width = btn_genisligi,
                    height=2,
                    font = "Verdana,Tahoma,DejaVuSans,LiberationSans,Ubuntu 10 bold",
                    bg = arkaplan_rengi_buton,
                    fg = "white",
                    state = "disable",
                    command= kaydet)
btn_kaydet.grid(row=4, column=0, padx=5, pady=5)

btn_kapat = tk.Button(pencere,
                    text = "Kapat",
                    width = btn_genisligi,
                    height=2,
                    font = "Verdana,Tahoma,DejaVuSans,LiberationSans,Ubuntu 10 bold",
                    bg = "#cd6155",
                    fg = "white",
                    command=quit)
btn_kapat.grid(row=4, column=1, padx=5, pady=5)

pencere.mainloop()