import tkinter as tk
import cv2
from PIL import Image
from PIL import ImageTk
from tkinter import SUNKEN, filedialog

print("Aplicatia ruleaza!")
def select_image():
    global panelA, panelB, entry
    print("Selectam imaginea!")
    path = filedialog.askopenfilename()  # salveaza path ul imaginii selectate
    imagine = cv2.imread(path)  # Pozele alese sunt standard 1920x1080

    imagineRedimensionata = cv2.resize(imagine, (640, 360))  # 1920x1080 : 3 // momentat x3 mai mica //480, 270 x4 mai mica
    gray = cv2.cvtColor(imagineRedimensionata, cv2.COLOR_BGR2GRAY)  # aplicam filtru gri peste imaginea reimensionata
    blur = cv2.GaussianBlur(gray, (11, 11), 0)  # aplicam blur peste imaginea reimensionata
    canny = cv2.Canny(blur, 30, 100)
    dilated = cv2.dilate(canny, (1, 1), iterations=0)
    cnt, hierarchy = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(imagineRedimensionata, cv2.COLOR_BGR2RGB)
    rgb2 = cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

    imagineRedimensionata = Image.fromarray(imagineRedimensionata)
    imagineRedimensionata = ImageTk.PhotoImage(imagineRedimensionata)

    rgb2 = Image.fromarray(rgb2)
    rgb2 = ImageTk.PhotoImage(rgb2)

    panelA = tk.Label(image=imagineRedimensionata)
    panelA.image = imagineRedimensionata
    panelA.grid(row=0, column=0)

    panelB = tk.Label(image=rgb2)
    panelB.image = rgb2
    panelB.grid(row=0, column=1)

    entry = tk.Entry(width=30)
    entry.grid(row=1, column=0, columnspan=2)
    entry.insert(0, 'Numărul de obiecte: ')
    entry.delete(20, tk.END)
    entry.insert(20, len(cnt))


window = tk.Tk()
window.title("Metode de contorizare automata numar aparitii in imagini - Nicola Darius")
panelA = None
panelB = None
entry = None
button = tk.Button(text="Selectați o imagine", width=40, relief=SUNKEN, command=select_image)
button.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
print("Aplicatia s-a inchis!")