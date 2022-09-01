from tkinter import *
from tkinter import messagebox
import sql_funcs


ws = Tk()
ws.title('login Douanier')
ws.config(bg='#0B5A81')


f = ('Times', 14)

right_frame = Frame( ws, bd=2,bg='#CCCCCC',relief=SOLID,padx=10,pady=10)
right_frame.pack()

def validateLoginLive(login_cin,login_motdepasse):

    cin = login_cin
    motdepasse = login_motdepasse
    all_douaniers = sql_funcs.select_douanier()
    bool_value = False
    login_bool = False
    for douanier in all_douaniers :
        douanier_cin = douanier[1]

        if douanier_cin == cin :
            bool_value = True
            douanier_motdepasse = douanier[8]

            if douanier_cin == cin and douanier_motdepasse == motdepasse :
                login_bool = True
            else :
                messagebox.showerror("error", 'mot de passe est incorrect ')

    if bool_value == False :
        messagebox.showerror("error", 'cin nexist pas dans le system ')


    # this is to open the next page
    if login_bool == True :
        pass

    return 0

def login_page(right_frame):
    Label(right_frame,text="username ",bg='#CCCCCC',font=f).grid(row=0, column=0, sticky=W, pady=10)
    login_cin = Entry(right_frame,font=f)
    login_cin.grid(row=0, column=1, pady=10, padx=20)


    Label(right_frame,text="mot de passe ",bg='#CCCCCC',font=f).grid(row=1, column=0, sticky=W, pady=10)
    login_motdepasse = Entry(right_frame,font=f, show='*')
    login_motdepasse.grid(row=1, column=1, pady=10, padx=20)


    login_btn = Button(right_frame,width=5,text='Login', font=f,relief=SOLID,cursor='hand2',command=lambda : validateLoginLive(login_cin.get(),login_motdepasse.get()))
    login_btn.grid(row=10, column=1, pady=10, padx=20)


    register_btn = Button(right_frame,width=15,text='Register', font=f,relief=SOLID,cursor='hand2',command=None)
    register_btn.grid(row=15, column=1, pady=10, padx=20)

    return 0


login_page(right_frame)


ws.mainloop()