import random
import string
import tkinter as tk

historik_liste = []
dark_mode = False

def opdater_ui_farver():
    bg = "#1e1e1e" if dark_mode else "white"
    fg = "white" if dark_mode else "black"
    entry_bg = "#2b2b2b" if dark_mode else "white"
    btn_bg = "#333333" if dark_mode else "white"

    vindue.config(bg=bg)

    for w in vindue.winfo_children():
        try:
            if isinstance(w, tk.Button):
                w.config(
                    bg=btn_bg,
                    fg=fg,
                    activebackground=btn_bg,
                    activeforeground=fg,
                    relief="flat"
                )
            elif isinstance(w, tk.Label):
                w.config(bg=bg, fg=fg)
            elif isinstance(w, tk.Checkbutton):
                w.config(bg=bg, fg=fg, selectcolor=bg, activebackground=bg)
            elif isinstance(w, tk.Scale):
                w.config(bg=bg, fg=fg, troughcolor=bg)
            elif isinstance(w, tk.Entry):
                w.config(bg=entry_bg, fg=fg, insertbackground=fg)
        except:
            pass

def vurder_styrke(kode):
    score = 0
    if any(c.islower() for c in kode): score += 1
    if any(c.isupper() for c in kode): score += 1
    if any(c.isdigit() for c in kode): score += 1
    if any(c in string.punctuation for c in kode): score += 1

    return "Svag" if score <= 1 else "Medium" if score == 2 else "Stærk"

def generer_kode():
    længde = længde_slider.get()

    tegn = string.ascii_letters + string.digits
    if special_var.get():
        tegn += string.punctuation

    kode = "".join(random.choice(tegn) for _ in range(længde))

    resultat.delete(0, tk.END)
    resultat.insert(0, kode)

    vindue.clipboard_clear()
    vindue.clipboard_append(kode)

    styrke_label.config(text=f"Styrke: {vurder_styrke(kode)}")

    historik_liste.insert(0, kode)
    if len(historik_liste) > 5:
        historik_liste.pop()

    historik_label.config(text="\n".join(historik_liste))

def clear_historik():
    historik_liste.clear()
    historik_label.config(text="")

def export_historik():
    with open("historik.txt", "w") as f:
        for k in historik_liste:
            f.write(k + "\n")

vindue = tk.Tk()
vindue.title("Kode generator")
vindue.geometry("360x450")

tk.Label(vindue, text="Længde").pack()

længde_slider = tk.Scale(vindue, from_=4, to=50, orient="horizontal")
længde_slider.set(16)
længde_slider.pack()

special_var = tk.BooleanVar()
tk.Checkbutton(vindue, text="Inkluder specialtegn", variable=special_var).pack()

tk.Button(vindue, text="Generer kode", command=generer_kode).pack(pady=10)

resultat = tk.Entry(vindue, font=("Arial", 16), justify="center")
resultat.pack()

styrke_label = tk.Label(vindue, text="Styrke: -")
styrke_label.pack()

tk.Label(vindue, text="Historik (sidste 5)").pack()
historik_label = tk.Label(vindue, text="")
historik_label.pack()

tk.Button(vindue, text="Ryd historik", command=clear_historik).pack(pady=5)
tk.Button(vindue, text="Export historik", command=export_historik).pack(pady=5)

vindue.mainloop()