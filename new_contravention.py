

from tkinter import *
from tkinter import messagebox
import sql_funcs
import random


ws = Tk()
ws.title('Douane')
ws.config(bg='#0B5A81')


f = ('Times', 14)

right_frame = Frame( ws, bd=2,bg='#CCCCCC',relief=SOLID,padx=10,pady=10)
right_frame.pack()

def get_random_douanier() :

    directeur_tab = []
    sous_directeur_tab = []
    reviseur_tab = []
    inspecteur_tab = []

    all_douanier = sql_funcs.select_douanier()
    for douanier in all_douanier :

        letype  = douanier[7]
        if letype == "directeur":
            directeur_tab.append(douanier)
        if letype == "sous_directeur":
            sous_directeur_tab.append(douanier)
        if letype == "reviseur":
            reviseur_tab.append(douanier)
        if letype == "inspecteur":
            inspecteur_tab.append(douanier)

    douanier1 = random.choice(inspecteur_tab)[1]
    douanier2 = random.choice(reviseur_tab)[1]
    douanier3 = random.choice(sous_directeur_tab)[1]
    douanier4 = random.choice(directeur_tab)[1]


    return [douanier1,douanier2,douanier3,douanier4]



def add_new_contravention( refnumbureau_info , datecreation_info,  region ,  procuration_info , proc_cin_original_info,cin_info,nom_info,prenom_info,email_info,address_info,gsm_info):


    comment1 = ""
    comment2 = ""
    comment3 = ""
    comment4 = ""

    commentstat1 = False
    commentstat2 = False
    commentstat3 = False
    commentstat4 = False

    from datetime import datetime
    now = datetime.now()

    refnumbureau = refnumbureau_info
    datecreation = datecreation_info
    regioncreation = region




    procuration = procuration_info
    proc_cin_original = proc_cin_original_info
    cin = cin_info
    nom = nom_info
    prenom = prenom_info
    email = email_info
    address = address_info
    gsm = gsm_info


    numseq = str(str(cin)+str(now))
    numseq = numseq.replace(" ","-")
    numseq = numseq.replace(":","-")

    not_empty_bool = len(refnumbureau) != 0 and len(datecreation) != 0 and len(regioncreation) != 0 and len(procuration) != 0 and len(proc_cin_original) != 0 and len(cin) != 0 and len(nom) != 0 and len(prenom) != 0 and len(email) != 0 and len(address) != 0 and len(gsm) != 0 and len(numseq) != 0
    if not_empty_bool :
        all_douaniers= get_random_douanier()


        doaunier1 = all_douaniers[0]
        douanier2 = all_douaniers[1]
        douanier3 = all_douaniers[2]
        douanier4 = all_douaniers[3]


        data_contrevenant = [procuration,proc_cin_original,cin,
                              nom, prenom, email, address,  gsm, numseq]

        data_contravention = [ refnumbureau, datecreation, regioncreation,
                               comment1, comment2, comment3, comment4,
                               doaunier1, douanier2, douanier3, douanier4,
                               commentstat1, commentstat2, commentstat3, commentstat4,
                               numseq]


        sql_funcs.insert_into_contrevenant(data_contrevenant)
        sql_funcs.insert_into_contravention(data_contravention)
    else:
        messagebox.showerror("error","il fault le remplir tous les champs")
    return 0


def new_contravention(right_frame) :
    Label(right_frame,text="num ref bureau ",bg='#CCCCCC',font=f).grid(row=0, column=0, sticky=W, pady=10)
    refnumbureau_info = Entry(right_frame,font=f)
    refnumbureau_info.grid(row=0, column=1, pady=10, padx=20)

    Label(right_frame,text="date creation ",bg='#CCCCCC',font=f).grid(row=1, column=0, sticky=W, pady=10)
    datecreation_info = Entry(right_frame,font=f)
    datecreation_info.grid(row=1, column=1, pady=10, padx=20)


    Label(right_frame,text="region  ",bg='#CCCCCC',font=f).grid(row=2, column=0, sticky=W, pady=10)
    region = Entry(right_frame,font=f)
    region.grid(row=2, column=1, pady=10, padx=20)


    Label(right_frame,text="procuration ",bg='#CCCCCC',font=f).grid(row=3, column=0, sticky=W, pady=10)
    procuration_info = Entry(right_frame,font=f)
    procuration_info.grid(row=3, column=1, pady=10, padx=20)

    Label(right_frame,text="cin original ",bg='#CCCCCC',font=f).grid(row=4, column=0, sticky=W, pady=10)
    proc_cin_original_info = Entry(right_frame,font=f)
    proc_cin_original_info.grid(row=4, column=1, pady=10, padx=20)


    Label(right_frame,text="cin ",bg='#CCCCCC',font=f).grid(row=5, column=0, sticky=W, pady=10)
    cin_info = Entry(right_frame,font=f)
    cin_info.grid(row=5, column=1, pady=10, padx=20)


    Label(right_frame,text="nom ",bg='#CCCCCC',font=f).grid(row=6, column=0, sticky=W, pady=10)
    nom_info = Entry(right_frame,font=f)
    nom_info.grid(row=6, column=1, pady=10, padx=20)

    Label(right_frame,text="prenom ",bg='#CCCCCC',font=f).grid(row=7, column=0, sticky=W, pady=10)
    prenom_info = Entry(right_frame,font=f)
    prenom_info.grid(row=7, column=1, pady=10, padx=20)

    Label(right_frame,text="email ",bg='#CCCCCC',font=f).grid(row=8, column=0, sticky=W, pady=10)
    email_info = Entry(right_frame,font=f)
    email_info.grid(row=8, column=1, pady=10, padx=20)

    Label(right_frame,text="address ",bg='#CCCCCC',font=f).grid(row=9, column=0, sticky=W, pady=10)
    address_info = Entry(right_frame,font=f)
    address_info.grid(row=9, column=1, pady=10, padx=20)

    Label(right_frame,text="gsm ",bg='#CCCCCC',font=f).grid(row=10, column=0, sticky=W, pady=10)
    gsm_info = Entry(right_frame,font=f)
    gsm_info.grid(row=10, column=1, pady=10, padx=20)



    nouv_contra_btn = Button(right_frame,width=15,text='Ajouter', font=f,relief=SOLID,cursor='hand2',command=lambda : add_new_contravention( refnumbureau_info.get() , datecreation_info.get() ,  region.get() ,  procuration_info.get() , proc_cin_original_info.get(),cin_info.get(),nom_info.get(),prenom_info.get(),email_info.get(),address_info.get(),gsm_info.get()))
    nouv_contra_btn.grid(row=15, column=1, pady=10, padx=20)


    return 0

new_contravention(right_frame)

ws.mainloop()