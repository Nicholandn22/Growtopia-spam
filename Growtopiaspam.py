import pyautogui
import pygetwindow as gw
from random import randrange as rd
from tkinter import *
from tkinter import messagebox
import time

pyautogui.FAILSAFE = False

# Daftar warna untuk spamming dengan format Growtopia
colours = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'b', 'w', 'p', 'o', '^', '$', '#', '@', '!', 'q', 'e', 'c', 'r', 't', 'a', 's']
run = False

# Fungsi untuk memeriksa apakah Growtopia adalah window aktif
def is_growtopia_active():
    try:
        win = gw.getActiveWindow()
        if win and "Growtopia" in win.title:  # Pastikan window yang aktif adalah Growtopia
            return True
        else:
            return False
    except Exception as e:
        return False

# Fungsi untuk memfokuskan window Growtopia
def focus_growtopia():
    try:
        # Dapatkan window Growtopia jika ada
        growtopia_window = None
        for win in gw.getWindowsWithTitle('Growtopia'):
            growtopia_window = win
            break
        if growtopia_window:
            growtopia_window.activate()  # Fokuskan Growtopia
    except Exception as e:
        print(f"Error focusing Growtopia: {e}")

# Fungsi untuk mulai spam
def start():
    global run
    if not txtfld.get().strip():  # Periksa apakah teks spam kosong
        messagebox.showerror("Error", "Spam text tidak boleh kosong!")
        return
    try:
        interval_value = int(interval.get())  # Konversi interval menjadi integer
        if interval_value <= 0:
            raise ValueError("Interval tidak boleh 0 atau negatif.")
    except ValueError:
        messagebox.showerror("Error", "Interval harus berupa angka positif (milidetik)!")  # Tampilkan pesan error
        return

    run = True
    window.after(2000, spam)

# Fungsi untuk menghentikan spam
def stop():
    global run
    run = False

# Fungsi untuk melakukan spam
def spam():
    global run
    try:
        delay = int(interval.get())  # Ambil interval untuk delay
    except ValueError:
        delay = 1000  # Gunakan default 1000ms jika interval tidak valid

    if run:
        focus_growtopia()  # Fokuskan Growtopia sebelum mengetik pesan
        pyautogui.press("enter")  # Tekan tombol Enter

        text = txtfld.get()
        if rcl.get():  # Jika opsi "Random colors" dipilih
            words = text.split()
            if words:
                # Membuat teks berwarna acak dan mengetikkan teks tersebut
                colored_text = ''.join([f" `{colours[rd(0, len(colours))]}{word}" for word in words])
                pyautogui.typewrite(colored_text[1:])  # Mulai dari indeks 1 untuk menghindari spasi pertama
        else:
            pyautogui.typewrite(text)  # Ketikkan teks tanpa warna acak

        pyautogui.press("enter")  # Tekan Enter lagi setelah mengetik
        window.after(delay, spam)  # Lanjutkan spam setelah delay yang diberikan

# Membuat antarmuka pengguna dengan Tkinter
window = Tk()
rcl = BooleanVar()  # Variabel untuk random colors

btn = Button(window, text="Start spamming", fg='green', command=start)
btn.place(x=94, y=85)
stopbtn = Button(window, text="Stop spamming", fg='red', command=stop)
stopbtn.place(x=94, y=115)

txtfld = Entry(window, bd=2)
txtfld.place(x=80, y=40)
txtfld.insert(0, 'Text a b c d s ')  # Teks default

interval = Entry(window, bd=2)
interval.place(x=80, y=60)
interval.insert(0, 5000)  # Interval default 5000ms (5 detik)

txl = Label(window, text='Spam text')
txl.place(x=20, y=40)

txl = Label(window, text='Interval')
txl.place(x=20, y=60)

main = Label(window, text='Growtopia spam')
main.place(x=80, y=10)

clr = Checkbutton(text='Random colors', variable=rcl, onvalue=rcl.set(True), offvalue=rcl.set(False))
clr.place(x=80, y=160)

window.title('Growtopia simple spam')
window.geometry("300x200+10+10")  # Ukuran window
window.mainloop()
