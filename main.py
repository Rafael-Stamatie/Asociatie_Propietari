import tkinter as tk
import uuid
from tkinter import messagebox

import db

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200

ROOT_WINDOW = tk.Tk()
DB_SESSION = db.new_session("asociatie.db")


def adauga_imobil():
    window = tk.Toplevel(ROOT_WINDOW)
    window.title("Adaugă imobil / cladire rezidentială")

    # TODO: Adauga functie comuna sa nu mai fie cod duplicat ca cel de mai jos.

    tk.Label(window, text="Administrator").grid(
        row=0, column=0, columnspan=2, padx=10, pady=5)

    tk.Label(window, text="Nume:").grid(row=1, column=0, padx=10, pady=5)
    admin_nume = tk.Entry(window)
    admin_nume.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(window, text="Prenume:").grid(row=2, column=0, padx=10, pady=5)
    admin_prenume = tk.Entry(window)
    admin_prenume.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(window, text="Telefon:").grid(row=3, column=0, padx=10, pady=5)
    admin_telefon = tk.Entry(window)
    admin_telefon.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(window, text="Email:").grid(row=4, column=0, padx=10, pady=5)
    admin_email = tk.Entry(window)
    admin_email.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(window, text="Președinte").grid(
        row=5, column=0, columnspan=2, padx=10, pady=5)

    tk.Label(window, text="Nume:").grid(row=6, column=0, padx=10, pady=5)
    pres_nume = tk.Entry(window)
    pres_nume.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(window, text="Prenume:").grid(row=7, column=0, padx=10, pady=5)
    pres_prenume = tk.Entry(window)
    pres_prenume.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(window, text="Telefon:").grid(row=8, column=0, padx=10, pady=5)
    pres_telefon = tk.Entry(window)
    pres_telefon.grid(row=8, column=1, padx=10, pady=5)

    tk.Label(window, text="Email:").grid(row=9, column=0, padx=10, pady=5)
    pres_email = tk.Entry(window)
    pres_email.grid(row=9, column=1, padx=10, pady=5)

    tk.Label(window, text="Adresă bloc").grid(
        row=10, column=0, columnspan=2, padx=10, pady=5)

    tk.Label(window, text="Localitate:").grid(
        row=11, column=0, padx=10, pady=5)
    bloc_localitate = tk.Entry(window)
    bloc_localitate.grid(row=11, column=1, padx=10, pady=5)

    tk.Label(window, text="Strada:").grid(row=12, column=0, padx=10, pady=5)
    bloc_str = tk.Entry(window)
    bloc_str.grid(row=12, column=1, padx=10, pady=5)

    tk.Label(window, text="Număr:").grid(
        row=13, column=0, padx=10, pady=5)
    bloc_nr = tk.Entry(window)
    bloc_nr.grid(row=13, column=1, padx=10, pady=5)

    def confirm():
        admin_nume_value = admin_nume.get()
        admin_prenume_value = admin_prenume.get()
        admin_telefon_value = admin_telefon.get()
        admin_email_value = admin_email.get()

        if (not admin_nume_value or
                not admin_prenume_value or
                not admin_telefon_value or
                not admin_email_value):
            messagebox.showerror("Error", "Lipsesc date administrator")
            return

        pres_nume_value = pres_nume.get()
        pres_prenume_value = pres_prenume.get()
        pres_telefon_value = pres_telefon.get()
        pres_email_value = pres_email.get()

        if (not pres_nume_value or
                not pres_prenume_value or
                not pres_telefon_value or
                not pres_email_value):
            messagebox.showerror("Error", "Lipsesc date presedinte")
            return

        bloc_localitate_value = bloc_localitate.get()
        bloc_str_value = bloc_str.get()
        bloc_nr_value = bloc_nr.get()

        if (not bloc_localitate_value or
                not bloc_str_value or
                not bloc_nr_value):
            messagebox.showerror("Error", "Lipsesc date adresa bloc")
            return

        # TODO: Mai multa validare pentru fiecare field.

        try:
            imobil = db.Imobil(
                id=str(uuid.uuid4()),

                admin_nume=admin_nume_value,
                admin_prenume=admin_prenume_value,
                admin_telefon=admin_telefon_value,
                admin_email=admin_email_value,

                presedinte_nume=pres_nume_value,
                presedinte_prenume=pres_prenume_value,
                presedinte_telefon=pres_telefon_value,
                presedinte_email=pres_email_value,

                localitate=bloc_localitate_value,
                strada=bloc_str_value,
                numar=bloc_nr_value
            )
            DB_SESSION.add(imobil)
            DB_SESSION.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        window.destroy()

    confirm_button = tk.Button(window, text="Confirm", command=confirm)
    confirm_button.grid(row=14, column=0, columnspan=2, padx=10, pady=10)


def listeaza_imobile():
    window = tk.Toplevel(ROOT_WINDOW)
    window.title("Detalii imobile / cladiri rezidentiale")

    nr_coloana = 0

    # TODO: Refactorizeaza codul pentru a nu mai fi cod duplicat ca cel de
    # mai jos.

    tk.Label(window, text="Localitate").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    tk.Label(window, text="Strada").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    tk.Label(window, text="Numar imobil").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    tk.Label(window, text="Numar apartament").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    tk.Label(window, text="Medie index apa").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    tk.Label(window, text="Medie index curent").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    tk.Label(window, text="Medie index gaz").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    imobile = DB_SESSION.query(db.Imobil).all()

    nr_rand = 1
    for imobil in imobile:
        nr_coloana = 0
        apartamente = DB_SESSION.query(db.Apartament).filter(
            db.Apartament.imobil_id == imobil.id).all()

        total_index_apa = 0
        total_index_curent = 0
        total_index_gaz = 0
        total_locatari = 0
        for apartament in apartamente:
            total_index_apa += apartament.index_apa
            total_index_curent += apartament.index_curent
            total_index_gaz += apartament.index_gaz
            total_locatari += apartament.numar_locatari

        medie_index_apa = round(total_index_apa / total_locatari, 2)
        medie_index_curent = round(total_index_curent / total_locatari, 2)
        medie_index_gaz = round(total_index_gaz / total_locatari, 2)

        tk.Label(window, text=imobil.localitate).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        tk.Label(window, text=imobil.strada).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        tk.Label(window, text=imobil.numar).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        tk.Label(window, text=len(apartamente)).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        tk.Label(window, text=medie_index_apa).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        tk.Label(window, text=medie_index_curent).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        tk.Label(window, text=medie_index_gaz).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        button = tk.Button(
            window,
            text="adaugă apartament",
            command=lambda id_imobil=imobil.id: adauga_apartament(id_imobil))
        button.grid(row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        button = tk.Button(
            window,
            text="listează apartamente",
            command=lambda id_imobil=imobil.id: listeaza_apartamente(
                id_imobil))
        button.grid(row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        nr_rand += 1


def adauga_apartament(id_imobil):
    window = tk.Toplevel(ROOT_WINDOW)
    window.title("Adaugă apartament")

    # TODO: Adauga functie comuna sa nu mai fie cod duplicat ca cel de mai jos.

    tk.Label(window, text="Numar:").grid(row=0, column=0, padx=10, pady=5)
    numar = tk.Entry(window)
    numar.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(window, text="Numar locatari:").grid(
        row=1, column=0, padx=10, pady=5)
    numar_locatari = tk.Entry(window)
    numar_locatari.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(window, text="Proprietar nume:").grid(
        row=2, column=0, padx=10, pady=5)
    proprietar_nume = tk.Entry(window)
    proprietar_nume.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(window, text="Proprietar prenume:").grid(
        row=3, column=0, padx=10, pady=5)
    proprietar_prenume = tk.Entry(window)
    proprietar_prenume.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(window, text="Index apa:").grid(
        row=4, column=0, padx=10, pady=5)
    index_apa = tk.Entry(window)
    index_apa.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(window, text="Index curent:").grid(
        row=5, column=0, padx=10, pady=5)
    index_curent = tk.Entry(window)
    index_curent.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(window, text="Index gaz:").grid(
        row=6, column=0, padx=10, pady=5)
    index_gaz = tk.Entry(window)
    index_gaz.grid(row=6, column=1, padx=10, pady=5)

    def salveaza():
        numar_value = numar.get()
        numar_locatari_value = numar_locatari.get()

        proprietar_nume_value = proprietar_nume.get()
        proprietar_prenume_value = proprietar_prenume.get()

        index_apa_value = index_apa.get()
        index_curent_value = index_curent.get()
        index_gaz_value = index_gaz.get()

        if not numar_value:
            messagebox.showerror("Error", "Lipseste numarul apartamentului")
            return

        if not numar_locatari_value:
            messagebox.showerror("Error", "Lipseste numarul de locatari")
            return

        if not proprietar_nume_value or not proprietar_prenume_value:
            messagebox.showerror(
                "Error", "Lipsesc numele sau prenumele proprietarului")
            return

        if (not index_apa_value or
            not index_curent_value or
                not index_gaz_value):
            messagebox.showerror(
                "Error", "Lipsesc valorile la index apa / curent / gaz")
            return

        # TODO: Mai multa validare pentru fiecare field.

        try:
            apartament = db.Apartament(
                id=str(uuid.uuid4()),

                numar=numar_value,
                numar_locatari=numar_locatari_value,
                imobil_id=id_imobil,

                proprietar_nume=proprietar_nume_value,
                proprietar_prenume=proprietar_prenume_value,

                index_apa=index_apa_value,
                index_curent=index_curent_value,
                index_gaz=index_gaz_value)
            DB_SESSION.add(apartament)
            DB_SESSION.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        window.destroy()

    confirm_button = tk.Button(window, text="Salvează", command=salveaza)
    confirm_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)


def listeaza_apartamente(id_imobil):
    window = tk.Toplevel(ROOT_WINDOW)
    window.title("Detalii apartamente pentru imobil")

    nr_coloana = 0

    # TODO: Refactorizeaza codul pentru a nu mai fi cod duplicat ca cel de
    # mai jos.

    tk.Label(window, text="Numar apartament").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    tk.Label(window, text="Numar locatari").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    tk.Label(window, text="Proprietar nume").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    tk.Label(window, text="Proprietar prenume").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    tk.Label(window, text="Index apa").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    tk.Label(window, text="Index curent").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    tk.Label(window, text="Index gaz").grid(
        row=0, column=nr_coloana, padx=10, pady=15)
    nr_coloana += 1

    apartamente = DB_SESSION.query(db.Apartament).filter(
        db.Apartament.imobil_id == id_imobil).all()

    nr_rand = 1
    for apartament in apartamente:
        nr_coloana = 0

        tk.Label(window, text=apartament.numar).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        tk.Label(window, text=apartament.numar_locatari).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        tk.Label(window, text=apartament.proprietar_nume).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        tk.Label(window, text=apartament.proprietar_prenume).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        tk.Label(window, text=apartament.index_apa).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        tk.Label(window, text=apartament.index_curent).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        tk.Label(window, text=apartament.index_gaz).grid(
            row=nr_rand, column=nr_coloana, padx=10, pady=5)
        nr_coloana += 1

        nr_rand += 1


if __name__ == "__main__":
    ROOT_WINDOW.title("Asociație de proprietari")

    # Seteaza dimensiunea ferestrei
    screen_width = ROOT_WINDOW.winfo_screenwidth()
    screen_height = ROOT_WINDOW.winfo_screenheight()
    x = (screen_width - WINDOW_WIDTH) // 2
    y = (screen_height - WINDOW_HEIGHT) // 2
    ROOT_WINDOW.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")

    # Adauga imobil / cladire rezidentiala
    tk.Label(
        ROOT_WINDOW, text="Adaugă imobil / cladire rezidentială",
        padx=10, pady=10).grid(
            row=0, column=0)
    tk.Button(
        ROOT_WINDOW, text="adaugă", command=adauga_imobil).grid(
            row=0, column=1)

    # Listează imobile / cladiri rezidentiale
    tk.Label(
        ROOT_WINDOW, text="Listeaza imobile / cladiri rezidentiale",
        padx=10, pady=10).grid(
            row=1, column=0)
    tk.Button(
        ROOT_WINDOW, text="listează", command=listeaza_imobile).grid(
            row=1, column=1)

    # Ruleaza aplicatia
    ROOT_WINDOW.mainloop()
