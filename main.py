import random
import string
import tkinter as tk

def generer_kode():
    sværhedsgrad = valg.get()

    if sværhedsgrad == "let":
        tegn = string.ascii_lowercase
        længde = 6
    elif sværhedsgrad == "medium":
        tegn = string.ascii_letters + string.digits
        længde = 10
    else:
        tegn = string.ascii_letters + string.digits + string.punctuation
        længde = 14

    kode = "".join(random.choice(tegn) for _ in range(længde))

    resultat.delete(0, tk.END)
    resultat.insert(0, kode)

def kopiér():
    vindue.clipboard_clear()
    vindue.clipboard_append(resultat.get())

vindue = tk.Tk()
vindue.title("Kode generator")
vindue.geometry("300x200")

valg = tk.StringVar(value="let")

tk.Label(vindue, text="Vælg sværhedsgrad").pack()

tk.Radiobutton(vindue, text="Let", variable=valg, value="let").pack()
tk.Radiobutton(vindue, text="Medium", variable=valg, value="medium").pack()
tk.Radiobutton(vindue, text="Svær", variable=valg, value="svær").pack()

tk.Button(vindue, text="Generer kode", command=generer_kode).pack(pady=10)

resultat = tk.Entry(vindue, font=("Arial", 16), justify="center")
resultat.pack()

tk.Button(vindue, text="Kopiér", command=kopiér).pack(pady=5)

vindue.mainloop()