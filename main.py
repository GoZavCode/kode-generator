import random
import string
import tkinter as tk
from datetime import datetime

historik_liste = []

MØRK_BG  = "#1e1e2e"
PANEL_BG = "#2a2a3e"
ACCENT   = "#7c6af7"
TEKST    = "#cdd6f4"
SVAG     = "#f38ba8"
OK       = "#f9e2af"
STÆRK    = "#a6e3a1"

KNAP_BG  = "#ffffff"
KNAP_FG  = "#000000"

def styrke(kode, special):
    score = 0
    if len(kode) >= 12: score += 1
    if len(kode) >= 20: score += 1
    if any(c.isupper() for c in kode): score += 1
    if any(c.isdigit() for c in kode): score += 1
    if special: score += 1
    if score <= 2:
        return "Svag 🔴", SVAG
    elif score <= 3:
        return "Okay 🟡", OK
    else:
        return "Stærk 🟢", STÆRK

def generer_kode():
    længde = længde_slider.get()
    tvetydige = "0O1lI"
    tegn = string.ascii_letters + string.digits
    if special_var.get():
        tegn += string.punctuation
    if tvetydig_var.get():
        tegn = "".join(c for c in tegn if c not in tvetydige)
    kode = "".join(random.choice(tegn) for _ in range(længde))
    resultat_var.set(kode)
    vindue.clipboard_clear()
    vindue.clipboard_append(kode)
    tekst, farve = styrke(kode, special_var.get())
    styrke_label.config(text=f"Styrke: {tekst}", fg=farve)
    tidspunkt = datetime.now().strftime("%H:%M:%S")
    historik_liste.insert(0, (kode, tidspunkt))
    if len(historik_liste) > 5:
        historik_liste.pop()
    opdater_historik()
    kopier_feedback()

def kopier_feedback():
    kopier_knap.config(text="Kopieret! ✓", bg="#00c853", fg="#000000")
    vindue.after(1500, lambda: kopier_knap.config(text="Kopier", bg=KNAP_BG, fg=KNAP_FG))

def kopier_manuelt():
    kode = resultat_var.get()
    if kode:
        vindue.clipboard_clear()
        vindue.clipboard_append(kode)
        kopier_feedback()

def opdater_historik():
    linjer = "\n".join(f"{k}  [{t}]" for k, t in historik_liste)
    historik_label.config(text=linjer or "—")

def clear_historik():
    historik_liste.clear()
    opdater_historik()

def export_historik():
    with open("historik.txt", "w") as f:
        for k, t in historik_liste:
            f.write(f"{k}  [{t}]\n")
    export_knap.config(text="Gemt! ✓", bg="#00c853", fg="#000000")
    vindue.after(1500, lambda: export_knap.config(text="Export historik", bg=KNAP_BG, fg=KNAP_FG))

# ── Vindue ──────────────────────────────────────────
vindue = tk.Tk()
vindue.title("Kode generator")
vindue.geometry("420x520")
vindue.configure(bg=MØRK_BG)
vindue.resizable(False, False)

def lbl(forælder, tekst, **kw):
    return tk.Label(forælder, text=tekst, bg=kw.pop("bg", MØRK_BG),
                    fg=kw.pop("fg", TEKST), **kw)

def knap(forælder, tekst, cmd, **kw):
    return tk.Button(forælder, text=tekst, command=cmd,
                     bg=KNAP_BG, fg=KNAP_FG,
                     activebackground="#dddddd", activeforeground="#000000",
                     relief="flat", cursor="hand2",
                     font=kw.pop("font", ("Arial", 10, "bold")), **kw)

# ── Titel ────────────────────────────────────────────
lbl(vindue, "🔑  Kode Generator", font=("Arial", 16, "bold"), fg=ACCENT).pack(pady=(18, 4))

# ── Slider ───────────────────────────────────────────
slider_ramme = tk.Frame(vindue, bg=MØRK_BG)
slider_ramme.pack(fill="x", padx=30)
lbl(slider_ramme, "Længde:").pack(side="left")
længde_slider = tk.Scale(slider_ramme, from_=4, to=64, orient="horizontal",
                          bg=MØRK_BG, fg=TEKST, troughcolor=PANEL_BG,
                          highlightthickness=0, activebackground=ACCENT)
længde_slider.set(16)
længde_slider.pack(side="left", fill="x", expand=True)

# ── Checkboxes ───────────────────────────────────────
check_ramme = tk.Frame(vindue, bg=MØRK_BG)
check_ramme.pack(pady=4)

special_var  = tk.BooleanVar()
tvetydig_var = tk.BooleanVar()

for tekst, var in [
    ("Inkluder specialtegn", special_var),
    ("Ekskluder tvetydige tegn  (0 O 1 l I)", tvetydig_var),
]:
    tk.Checkbutton(check_ramme, text=tekst, variable=var,
                   bg=MØRK_BG, fg=TEKST, selectcolor=PANEL_BG,
                   activebackground=MØRK_BG, activeforeground=TEKST).pack(anchor="w")

# ── Generer-knap ─────────────────────────────────────
knap(vindue, "Generer kode", generer_kode,
     padx=20, pady=8, font=("Arial", 12, "bold")).pack(pady=10)

# ── Resultat + kopier ────────────────────────────────
res_ramme = tk.Frame(vindue, bg=MØRK_BG)
res_ramme.pack(padx=30, fill="x")

resultat_var = tk.StringVar()
resultat_entry = tk.Entry(res_ramme, textvariable=resultat_var,
                           font=("Courier", 13), justify="center",
                           bg=PANEL_BG, fg=TEKST, insertbackground=TEKST,
                           relief="flat", bd=6)
resultat_entry.pack(side="left", fill="x", expand=True)

kopier_knap = knap(res_ramme, "Kopier", kopier_manuelt, padx=10, pady=4)
kopier_knap.pack(side="left", padx=(6, 0))

# ── Styrke-indikator ─────────────────────────────────
styrke_label = lbl(vindue, "Styrke: —", font=("Arial", 10))
styrke_label.pack(pady=(6, 0))

# ── Historik ─────────────────────────────────────────
lbl(vindue, "Historik (sidste 5)", font=("Arial", 9, "bold"), fg=ACCENT).pack(pady=(14, 0))

historik_ramme = tk.Frame(vindue, bg=PANEL_BG, bd=0)
historik_ramme.pack(padx=30, fill="x", ipady=6)

historik_label = tk.Label(historik_ramme, text="—",
                           font=("Courier", 9), bg=PANEL_BG, fg=TEKST,
                           justify="left", anchor="w")
historik_label.pack(fill="x", padx=8)

# ── Bund-knapper ─────────────────────────────────────
knap_ramme = tk.Frame(vindue, bg=MØRK_BG)
knap_ramme.pack(pady=12)

knap(knap_ramme, "Ryd historik", clear_historik, padx=12, pady=6).pack(side="left", padx=6)

export_knap = knap(knap_ramme, "Export historik", export_historik, padx=12, pady=6)
export_knap.pack(side="left", padx=6)

vindue.mainloop()