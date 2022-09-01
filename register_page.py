from tkinter import *
from tkinter import messagebox
import sql_funcs


ws = Tk()
ws.title('Enregister Douanier')
ws.config(bg='#0B5A81')

f = ('Times', 14)


def validateLogin(  register_nummartricule,register_cin,register_nom, register_prenom, register_email,  register_address,  register_gsm,  register_type, register_pwd,pwd_again,adminuser,adminpwd ):
    nummartricule =register_nummartricule
    cin =    register_cin
    nom =    register_nom
    prenom =    register_prenom
    email =    register_email
    address =    register_address
    gsm =    register_gsm
    letype =    register_type

    motdepasse =    register_pwd
    motdepasse_again = pwd_again

    admin_user = adminuser
    admin_password = adminpwd



    if str(motdepasse_again) == str(motdepasse)   :
        data = [nummartricule, cin, nom, prenom, email, address, gsm, letype, motdepasse]
        all_douanier_data = sql_funcs.select_douanier()
        all_douanier_data.pop(0)
        not_empty = len(nummartricule)!=0 and len(cin)!=0 and len(nom)!=0 and len(prenom)!=0 and len(email)!=0 and len(address)!=0 and len(gsm)!=0     and len(gsm)!=0 and len(letype)!=0 and len(motdepasse)!=0
        if not_empty == True :
            for elem in all_douanier_data :
                old_cin = elem[1]
                if old_cin == cin :
                    messagebox.showerror("error", 'ce CIN est deja existe dans le system')

            for elem in all_douanier_data :
                letype = elem[7]
                if str(letype) == "directeur" :
                    admin_pass = elem[8]
                    admin_cin = elem[1]
                    if str(admin_pass) == str(admin_password) and str(admin_cin) == str(admin_user)   :
                        sql_funcs.insert_into_douanier(data)
                        pass
                    else :
                        messagebox.showerror("error",'le mot de passe de directeur est incorrect')
        else:
            messagebox.showerror("error", 'il faut de remplir tous la formulaire')
    else:
        messagebox.showerror("error", 'les deux mode de passe ne sont pas similaire')

    print(data)
    return


right_frame = Frame( ws, bd=2,bg='#CCCCCC',relief=SOLID,padx=10,pady=10)
right_frame.pack()

def register_page(right_frame) :


    Label(right_frame,text="cin ",bg='#CCCCCC',font=f).grid(row=0, column=0, sticky=W, pady=10)
    register_cin = Entry(right_frame,font=f)
    register_cin.grid(row=0, column=1, pady=10, padx=20)


    Label(right_frame,text="nom ",bg='#CCCCCC',font=f).grid(row=1, column=0, sticky=W, pady=10)
    register_nom = Entry(right_frame,font=f)
    register_nom.grid(row=1, column=1, pady=10, padx=20)

    Label(right_frame,text="prenom ",bg='#CCCCCC',font=f).grid(row=2, column=0, sticky=W, pady=10)
    register_prenom = Entry(right_frame,font=f)
    register_prenom.grid(row=2, column=1, pady=10, padx=20)

    Label(right_frame,text="email ",bg='#CCCCCC',font=f).grid(row=3, column=0, sticky=W, pady=10)
    register_email = Entry(right_frame,font=f)
    register_email.grid(row=3, column=1, pady=10, padx=20)

    Label(right_frame,text="address ",bg='#CCCCCC',font=f).grid(row=4, column=0, sticky=W, pady=10)
    register_address = Entry(right_frame,font=f)
    register_address.grid(row=4, column=1, pady=10, padx=20)

    Label(right_frame,text="gsm ",bg='#CCCCCC',font=f).grid(row=5, column=0, sticky=W, pady=10)
    register_gsm = Entry(right_frame,font=f)
    register_gsm.grid(row=5, column=1, pady=10, padx=20)

    Label(right_frame,text="type ",bg='#CCCCCC',font=f).grid(row=6, column=0, sticky=W, pady=10)
    register_type = Entry(right_frame,font=f)
    register_type.grid(row=6, column=1, pady=10, padx=20)


    Label( right_frame, text="Enter mot de passe", bg='#CCCCCC',font=f).grid(row=7, column=0, sticky=W, pady=10)
    register_pwd = Entry( right_frame,font=f,show='*')
    register_pwd.grid(row=7, column=1, pady=10, padx=20)

    Label(right_frame,text="Re-Enter mot de passe",bg='#CCCCCC',font=f).grid(row=8, column=0, sticky=W, pady=10)
    pwd_again = Entry( right_frame, font=f, show='*')
    pwd_again.grid(row=8, column=1, pady=10, padx=20)


    Label(right_frame,text="numero matricule",bg='#CCCCCC',font=f).grid(row=9, column=0, sticky=W, pady=10)
    register_nummartricule = Entry( right_frame, font=f)
    register_nummartricule.grid(row=9, column=1, pady=10, padx=20)

    Label(right_frame,text="admin login ",bg='#CCCCCC',font=f).grid(row=11, column=0, sticky=W, pady=10)
    adminuser = Entry(right_frame,font=f)
    adminuser.grid(row=11, column=1, pady=10, padx=20)

    Label(right_frame,text="admin motdepasse ",bg='#CCCCCC',font=f).grid(row=12, column=0, sticky=W, pady=10)
    adminpwd = Entry(right_frame,font=f, show='*')
    adminpwd.grid(row=12, column=1, pady=10, padx=20)


    register_btn = Button(right_frame,width=15,text='Register', font=f,relief=SOLID,cursor='hand2',command=lambda : validateLogin(   register_nummartricule.get(),register_cin.get(),register_nom.get(), register_prenom.get(), register_email.get(),  register_address.get(),  register_gsm.get(),  register_type.get(), register_pwd.get(),pwd_again.get(),adminuser.get(),adminpwd.get()))
    register_btn.grid(row=15, column=1, pady=10, padx=20)



register_page(right_frame)


ws.mainloop()