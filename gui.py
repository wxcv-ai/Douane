from tkinter import *
from tkinter import messagebox
import sql_funcs
import random
from PIL import Image, ImageTk
import tkinter  as tk
from tkinter import ttk

f = ('Times', 12)


def rasie_frame(frame):
    frame.tkraise()

def upper_buttons(right_frame,current_doaunier):
    def determiner_le_role(current_cin):
        all_douaniers = sql_funcs.select_douanier()
        for douanier in all_douaniers:
            douanier_cin = douanier[1]
            if douanier_cin == current_cin:
                current_type = douanier[7]
        string = ""
        if current_type == "directeur":
            string = " repmlir le commentair N4"

        if current_type == "sous_directeur":
            string = " repmlir le commentair N3"

        if current_type == "reviseur":
            string = " repmlir le commentair N2"

        if current_type == "inspecteur":
            string = " repmlir le commentair N1"

        return string

    def get_douanier_contrav(douanier_cin):

        douanier_data = sql_funcs.select_douanier()

        doaunier_elemnts = []
        global_douanier_type = ""
        for elem in douanier_data:
            cin = elem[1]
            if str(cin) == str(douanier_cin):
                letype = elem[7]
                global_douanier_type = letype

        if len(global_douanier_type) != 0:

            all_data_contravention = sql_funcs.select_contravention()
            for data_contravention in all_data_contravention:
                doaunier1 = data_contravention[7]
                douanier2 = data_contravention[8]
                douanier3 = data_contravention[9]
                douanier4 = data_contravention[10]

                commentstat1 = data_contravention[11]
                commentstat2 = data_contravention[12]
                commentstat3 = data_contravention[13]
                commentstat4 = data_contravention[14]
                numseq = data_contravention[15]

                if global_douanier_type == "directeur":
                    if (str(commentstat4)) == "False" and douanier4 == douanier_cin:
                        doaunier_elemnts.append(numseq)
                if global_douanier_type == "sous_directeur":
                    if (str(commentstat3)) == "False" and douanier3 == douanier_cin:
                        doaunier_elemnts.append(numseq)
                if global_douanier_type == "reviseur":
                    if (str(commentstat2)) == "False" and douanier2 == douanier_cin:
                        doaunier_elemnts.append(numseq)
                if global_douanier_type == "inspecteur":

                    if (str(commentstat1)) == "False" and doaunier1 == douanier_cin:
                        doaunier_elemnts.append(numseq)

        return doaunier_elemnts

    def get_all_data(numseq):

        data_contravention = sql_funcs.select_contravention_specific(numseq)

        refnumbureau = data_contravention[1]
        datecreation = data_contravention[2]
        regioncreation = data_contravention[3]

        comment1 = data_contravention[4]
        comment2 = data_contravention[5]
        comment3 = data_contravention[6]
        comment4 = data_contravention[7]

        doaunier1 = data_contravention[8]
        douanier2 = data_contravention[9]
        douanier3 = data_contravention[10]
        douanier4 = data_contravention[11]

        commentstat1 = data_contravention[12]
        commentstat2 = data_contravention[13]
        commentstat3 = data_contravention[0]
        commentstat4 = data_contravention[14]

        numseq = data_contravention[15]

        data_contrevenant = sql_funcs.select_contrevenant_specific(numseq)

        procuration = data_contrevenant[0]
        proc_cin_original = data_contrevenant[1]
        cin = data_contrevenant[2]
        nom = data_contrevenant[3]
        prenom = data_contrevenant[4]
        email = data_contrevenant[5]
        address = data_contrevenant[6]
        gsm = data_contrevenant[7]
        numseq = data_contrevenant[8]

        return [refnumbureau, datecreation, regioncreation, comment1, comment2, comment3, comment4, doaunier1,
                douanier2, douanier3, douanier4, commentstat1, commentstat2, commentstat3, commentstat4, procuration,
                proc_cin_original, cin, nom, prenom, email, address, gsm]

    def update_comment(index, current_cin, numseq, data):
        all_douaniers = sql_funcs.select_douanier()
        for douanier in all_douaniers:
            douanier_cin = douanier[1]
            if douanier_cin == current_cin:
                current_type = douanier[7]
        if current_type == "directeur":
            if index == 4:
                comment_name = "comment4"
                comment_data = data[3]
                comment_boolean = "commentstat4"

                data = [comment_name, comment_data, comment_boolean, numseq]
                sql_funcs.update_contravention(data)
        if current_type == "sous_directeur":
            if index == 3:
                comment_name = "comment3"
                comment_data = data[2]
                comment_boolean = "commentstat3"
                data = [comment_name, comment_data, comment_boolean, numseq]
                sql_funcs.update_contravention(data)
        if current_type == "reviseur":
            if index == 2:
                comment_name = "comment2"
                comment_data = data[1]
                comment_boolean = "commentstat2"

                data = [comment_name, comment_data, comment_boolean, numseq]
                sql_funcs.update_contravention(data)
        if current_type == "inspecteur":
            if index == 1:
                comment_name = "comment1"
                comment_data = data[0]
                comment_boolean = "commentstat1"

                data = [comment_name, comment_data, comment_boolean, numseq]
                sql_funcs.update_contravention(data)
        return 0

    def orgnize_douaniers_data(current_doaunier):

        douanier_cntraves = get_douanier_contrav(current_doaunier)

        if len(douanier_cntraves) > 3:
            douanier_cntraves = douanier_cntraves[0:2]
        elif len(douanier_cntraves) == 3:
            pass
        else:
            num = 3 - len(douanier_cntraves)
            for i in range(0, num):
                douanier_cntraves.append(0)
        return douanier_cntraves
    logo_btn = ttk.Button(right_frame, width=2, image=logo, command=None).grid(row=0, column=5)

    Label(right_frame, text=determiner_le_role(current_doaunier), bg='#CCCCCC', font=f).grid(row=0, column=3, sticky=W, pady=10)

    logout_btn = Button(right_frame,width=15,text='log out', font=f,relief=SOLID,cursor='hand2',command=lambda : rasie_frame((login_page_frame)))
    logout_btn.grid(row=0, column=1, pady=10, padx=20)
    ajouter_contravention = Button(right_frame,width=15,text='ajouter contravention',bg= "#c9c230", font=f,relief=SOLID,cursor='hand2',command=lambda : rasie_frame((add_contravention_page_frame)))
    ajouter_contravention.grid(row=0, column=2, pady=10, padx=20)
    return 0

def main_page(i,right_frame,current_doaunier):
    def determiner_le_role(current_cin):
        all_douaniers = sql_funcs.select_douanier()
        for douanier in all_douaniers:
            douanier_cin = douanier[1]
            if douanier_cin == current_cin:
                current_type = douanier[7]

        if current_type == "directeur":
            string = " repmlir le commentair N4"

        if current_type == "sous_directeur":
            string = " repmlir le commentair N3"

        if current_type == "reviseur":
            string = " repmlir le commentair N2"

        if current_type == "inspecteur":
            string = " repmlir le commentair N1"

        return string

    def determiner_le_role_num(current_cin):
        all_douaniers = sql_funcs.select_douanier()
        for douanier in all_douaniers:
            douanier_cin = douanier[1]
            if douanier_cin == current_cin:
                current_type = douanier[7]
        num = 0
        if current_type == "directeur":
            num = 4

        if current_type == "sous_directeur":
            num = 3

        if current_type == "reviseur":
            num = 2

        if current_type == "inspecteur":
            num = 1

        return num

    def get_douanier_contrav(douanier_cin):

        douanier_data = sql_funcs.select_douanier()

        doaunier_elemnts = []
        global_douanier_type = ""
        for elem in douanier_data:
            cin = elem[1]
            if str(cin) == str(douanier_cin):
                letype = elem[7]
                global_douanier_type = letype

        if len(global_douanier_type) != 0:

            all_data_contravention = sql_funcs.select_contravention()
            for data_contravention in all_data_contravention:
                doaunier1 = data_contravention[7]
                douanier2 = data_contravention[8]
                douanier3 = data_contravention[9]
                douanier4 = data_contravention[10]

                commentstat1 = data_contravention[11]
                commentstat2 = data_contravention[12]
                commentstat3 = data_contravention[13]
                commentstat4 = data_contravention[14]
                numseq = data_contravention[15]

                if global_douanier_type == "directeur":
                    if (str(commentstat4)) == "False" and douanier4 == douanier_cin:
                        doaunier_elemnts.append(numseq)
                if global_douanier_type == "sous_directeur":
                    if (str(commentstat3)) == "False" and douanier3 == douanier_cin:
                        doaunier_elemnts.append(numseq)
                if global_douanier_type == "reviseur":
                    if (str(commentstat2)) == "False" and douanier2 == douanier_cin:
                        doaunier_elemnts.append(numseq)
                if global_douanier_type == "inspecteur":

                    if (str(commentstat1)) == "False" and doaunier1 == douanier_cin:
                        doaunier_elemnts.append(numseq)

        return doaunier_elemnts

    def get_all_data(numseq):

        data_contravention = sql_funcs.select_contravention_specific(numseq)

        refnumbureau = data_contravention[1]
        datecreation = data_contravention[2]
        regioncreation = data_contravention[3]

        comment1 = data_contravention[4]
        comment2 = data_contravention[5]
        comment3 = data_contravention[6]
        comment4 = data_contravention[7]

        doaunier1 = data_contravention[8]
        douanier2 = data_contravention[9]
        douanier3 = data_contravention[10]
        douanier4 = data_contravention[11]

        commentstat1 = data_contravention[12]
        commentstat2 = data_contravention[13]
        commentstat3 = data_contravention[0]
        commentstat4 = data_contravention[14]

        numseq = data_contravention[15]

        data_contrevenant = sql_funcs.select_contrevenant_specific(numseq)

        procuration = data_contrevenant[0]
        proc_cin_original = data_contrevenant[1]
        cin = data_contrevenant[2]
        nom = data_contrevenant[3]
        prenom = data_contrevenant[4]
        email = data_contrevenant[5]
        address = data_contrevenant[6]
        gsm = data_contrevenant[7]
        numseq = data_contrevenant[8]

        return [refnumbureau, datecreation, regioncreation, comment1, comment2, comment3, comment4, doaunier1,
                douanier2, douanier3, douanier4, commentstat1, commentstat2, commentstat3, commentstat4, procuration,
                proc_cin_original, cin, nom, prenom, email, address, gsm]

    def update_comment(index, current_cin, numseq, data):
        all_douaniers = sql_funcs.select_douanier()
        for douanier in all_douaniers:
            douanier_cin = douanier[1]
            if douanier_cin == current_cin:
                current_type = douanier[7]
        if current_type == "directeur":
            if index == 4:
                comment_name = "comment4"
                comment_data = data[3]
                comment_boolean = "commentstat4"

                data = [comment_name, comment_data, comment_boolean, numseq]
                sql_funcs.update_contravention(data)
        if current_type == "sous_directeur":
            if index == 3:
                comment_name = "comment3"
                comment_data = data[2]
                comment_boolean = "commentstat3"
                data = [comment_name, comment_data, comment_boolean, numseq]
                sql_funcs.update_contravention(data)
        if current_type == "reviseur":
            if index == 2:
                comment_name = "comment2"
                comment_data = data[1]
                comment_boolean = "commentstat2"

                data = [comment_name, comment_data, comment_boolean, numseq]
                sql_funcs.update_contravention(data)
        if current_type == "inspecteur":
            if index == 1:
                comment_name = "comment1"
                comment_data = data[0]
                comment_boolean = "commentstat1"

                data = [comment_name, comment_data, comment_boolean, numseq]
                sql_funcs.update_contravention(data)
        return 0

    def orgnize_douaniers_data(current_doaunier):
        douanier_cntraves = get_douanier_contrav(current_doaunier)


        if len(douanier_cntraves) > 3:
            douanier_cntraves = douanier_cntraves[0:2]
        elif len(douanier_cntraves) == 3:
            pass
        elif len(douanier_cntraves) == 2:
            douanier_cntraves.append(0)
        elif len(douanier_cntraves) == 1:
            douanier_cntraves.append(0)
            douanier_cntraves.append(0)
        elif len(douanier_cntraves) == 0:
            douanier_cntraves.append(0)
            douanier_cntraves.append(0)
            douanier_cntraves.append(0)


        return douanier_cntraves

    douanier_cntraves = orgnize_douaniers_data(current_doaunier)


    numseq = douanier_cntraves[i]
    if (numseq)!= 0 :
        data_contravention = sql_funcs.select_contravention_specific(numseq)[0]

        refnumbureau = data_contravention[0]
        datecreation = data_contravention[1]
        regioncreation = data_contravention[2]


        comment1 = data_contravention[3]
        comment2 = data_contravention[4]
        comment3 = data_contravention[5]
        comment4 = data_contravention[6]

        doaunier1 = data_contravention[7]
        douanier2 = data_contravention[8]
        douanier3 = data_contravention[9]
        douanier4 = data_contravention[10]

        commentstat1 = data_contravention[11]
        commentstat2 = data_contravention[12]
        commentstat3 = data_contravention[13]
        commentstat4 = data_contravention[14]


        data_contrevenant = sql_funcs.select_contrevenant_specific(numseq)[0]

        procuration = data_contrevenant[0]
        proc_cin_original = data_contrevenant[1]
        cin = data_contrevenant[2]
        nom = data_contrevenant[3]
        prenom = data_contrevenant[4]
        email = data_contrevenant[5]
        address = data_contrevenant[6]
        gsm = data_contrevenant[7]

        Label(right_frame, text="nom prenom:", bg='#bf2525', font=f).grid(row=i*6+3, column=0, sticky=W, pady=10)
        Label(right_frame, text=nom +str("")+ prenom, bg='#CCCCCC', font=f).grid(row=i*6+3, column=1, sticky=W, pady=10)

        Label(right_frame,text="cin est:",bg='#bf2525',font=f).grid(row=i*6+4, column=0, sticky=W, pady=10)
        Label(right_frame,text=cin,bg='#CCCCCC',font=f).grid(row=i*6+4, column=1, sticky=W, pady=10)

        Label(right_frame,text="TEL:",bg='#bf2525',font=f).grid(row=i*6+5, column=0, sticky=W, pady=10)
        Label(right_frame,text=gsm,bg='#CCCCCC',font=f).grid(row=i*6+5, column=1, sticky=W, pady=10)

        Label(right_frame,text="procuraton:",bg='#bf2525',font=f).grid(row=i*6+6, column=0, sticky=W, pady=10)
        Label(right_frame,text=procuration,bg='#CCCCCC',font=f).grid(row=i*6+6, column=1, sticky=W, pady=10)


        Label(right_frame,text="cin original de:",bg='#bf2525',font=f).grid(row=i*6+3, column=2, sticky=W, pady=10)
        Label(right_frame,text=proc_cin_original,bg='#CCCCCC',font=f).grid(row=i*6+3, column=3, sticky=W, pady=10)


        Label(right_frame,text="date de creation:",bg='#bf2525',font=f).grid(row=i*6+4, column=2, sticky=W, pady=10)
        Label(right_frame,text=datecreation,bg='#CCCCCC',font=f).grid(row=i*6+4, column=3, sticky=W, pady=10)


        Label(right_frame,text="numero de bureau:",bg='#bf2525',font=f).grid(row=i*6+5, column=2, sticky=W, pady=10)
        Label(right_frame,text=refnumbureau,bg='#CCCCCC',font=f).grid(row=i*6+5, column=3, sticky=W, pady=10)

        Label(right_frame,text="region de creation:",bg='#bf2525',font=f).grid(row=i*6+6, column=2, sticky=W, pady=10)
        Label(right_frame,text=regioncreation,bg='#CCCCCC',font=f).grid(row=i*6+6, column=3, sticky=W, pady=10)
        role_num = determiner_le_role_num(current_doaunier)
        comment1 = data_contravention[3]
        comment2 = data_contravention[4]
        comment3 = data_contravention[5]
        comment4 = data_contravention[6]



        if (role_num == 1 or role_num == 2 or  role_num == 3 or role_num == 4 ) and len(comment1)!=0:
            Label(right_frame, text=comment1, bg='#CCCCCC', font=f).grid(row=i * 6 + 3, column=4, sticky=W,pady=10)
        else :
            Label(right_frame, text="commentaire 1:", bg='#CCCCCC', font=f).grid(row=i * 6 + 3, column=4, sticky=W,pady=10)

        comm1_input = Entry(right_frame, font=f)
        comm1_input.grid(row=i*6+3, column=5, pady=10, padx=20)
        send_btn = Button(right_frame, width=5, bg= "#c9c230", text='Send', font=f, relief=SOLID, cursor='hand2',command=lambda:update_comment(1,current_doaunier,numseq , [comm1_input.get(),comm2_input.get(),comm3_input.get(),comm4_input.get()]))
        send_btn.grid(row=i*6+3, column=6, pady=10, padx=20)


        if  role_num == 2 or role_num == 3 or role_num == 4 and len(comment2)!=0:
            Label(right_frame, text=comment2, bg='#CCCCCC', font=f).grid(row=i * 6 + 4, column=4, sticky=W,pady=10)
        else:
            Label(right_frame, text="commentaire 2:", bg='#CCCCCC', font=f).grid(row=i * 6 + 4, column=4, sticky=W,pady=10)
        comm2_input = Entry(right_frame, font=f)
        comm2_input.grid(row=i*6+4, column=5, pady=10, padx=20)
        send_btn = Button(right_frame, width=5, text='Send',bg= "#c9c230", font=f, relief=SOLID, cursor='hand2',command=lambda: update_comment(2,current_doaunier,numseq, [comm1_input.get(),comm2_input.get(),comm3_input.get(),comm4_input.get()]))
        send_btn.grid(row=i*6+4, column=6, pady=10, padx=20)

        if role_num == 3 or role_num == 4 and len(comment3)!=0:
            Label(right_frame, text=comment3, bg='#CCCCCC', font=f).grid(row=i * 6 + 5, column=4, sticky=W,pady=10)
        else:
            Label(right_frame, text="commentaire 3:", bg='#CCCCCC', font=f).grid(row=i * 6 + 5, column=4, sticky=W,
                                                                                 pady=10)
        comm3_input = Entry(right_frame, font=f)
        comm3_input.grid(row=i*6+5, column=5, pady=10, padx=20)
        send_btn = Button(right_frame, width=5, text='Send', bg= "#c9c230",font=f, relief=SOLID, cursor='hand2',command=lambda:update_comment(3,current_doaunier,numseq, [comm1_input.get(),comm2_input.get(),comm3_input.get(),comm4_input.get()]))
        send_btn.grid(row=i*6+5, column=6, pady=10, padx=20)

        if  role_num == 4 and len(comment4)!=0:
            Label(right_frame, text=comment4, bg='#CCCCCC', font=f).grid(row=i * 6 + 6, column=4, sticky=W,pady=10)
        else :
            Label(right_frame, text="commentaire 4:", bg='#CCCCCC', font=f).grid(row=i * 6 + 6, column=4, sticky=W,
                                                                                 pady=10)

        comm4_input = Entry(right_frame, font=f)
        comm4_input.grid(row=i*6+6, column=5, pady=10, padx=20)
        send_btn = Button(right_frame, width=5, text='Send', bg= "#c9c230",font=f, relief=SOLID, cursor='hand2',command=lambda: update_comment(4,current_doaunier,numseq, [comm1_input.get(),comm2_input.get(),comm3_input.get(),comm4_input.get()]))
        send_btn.grid(row=i*6+6, column=6, pady=10, padx=20)



def login_page(right_frame ):
    def validateLoginLive(login_cin, login_motdepasse):

        cin = login_cin

        motdepasse = login_motdepasse
        all_douaniers = sql_funcs.select_douanier()
        bool_value = False
        login_bool = False
        for douanier in all_douaniers:
            douanier_cin = douanier[1]

            if douanier_cin == cin:
                bool_value = True
                douanier_motdepasse = douanier[8]

                if douanier_cin == cin and douanier_motdepasse == motdepasse:
                    login_bool = True

                else:
                    messagebox.showerror("error", 'mot de passe est incorrect ')

        if bool_value == False:
            messagebox.showerror("error", 'cin nexist pas dans le system ')

        # this is to open the next page
        if login_bool == True:
            rasie_frame(main_page_frame)
            current_doaunier = login_cin
            upper_buttons(main_page_frame, current_doaunier)
            main_page(0, main_page_frame, current_doaunier)
            main_page(1, main_page_frame, current_doaunier)
            main_page(2, main_page_frame, current_doaunier)

            return current_doaunier
        else:
            return 0

    logo_btn = ttk.Button(right_frame, width=2, image=logo, command=None).grid(row=0, column=0)

    Label(right_frame,text="username ",bg='#CCCCCC',font=f).grid(row=0, column=1, sticky=W, pady=10)
    login_cin = Entry(right_frame,font=f)
    login_cin.grid(row=0, column=2, pady=10, padx=20)


    Label(right_frame,text="mot de passe ",bg='#CCCCCC',font=f).grid(row=1, column=1, sticky=W, pady=10)
    login_motdepasse = Entry(right_frame,font=f, show='*')
    login_motdepasse.grid(row=1, column=2, pady=10, padx=20)


    login_btn = Button(right_frame,width=5,text='Login', font=f,relief=SOLID,cursor='hand2',command=lambda : validateLoginLive(login_cin.get(),login_motdepasse.get() ))
    login_btn.grid(row=10, column=3, pady=10, padx=20)


    register_btn = Button(right_frame,width=15,text='Register', font=f,relief=SOLID,cursor='hand2',command=lambda : rasie_frame((register_page_frame)))
    register_btn.grid(row=10, column=1, pady=10, padx=20)

    return 0

def register_page(right_frame) :

    def validateLogin(register_nummartricule, register_cin, register_nom, register_prenom, register_email,register_address, register_gsm, register_type, register_pwd, pwd_again, adminuser, adminpwd):

        nummartricule = register_nummartricule
        cin = register_cin
        nom = register_nom
        prenom = register_prenom
        email = register_email
        address = register_address
        gsm = register_gsm
        letype = register_type

        motdepasse = register_pwd
        motdepasse_again = pwd_again

        admin_user = adminuser
        admin_password = adminpwd

        if str(motdepasse_again) == str(motdepasse):
            data = [nummartricule, cin, nom, prenom, email, address, gsm, letype, motdepasse]
            all_douanier_data = sql_funcs.select_douanier()
            #if len(all_douanier_data) != 0 and len(all_douanier_data)!=1 :
                #all_douanier_data.pop(0)

            not_empty = len(nummartricule) != 0 and len(cin) != 0 and len(nom) != 0 and len(prenom) != 0 and len(
                email) != 0 and len(address) != 0 and len(gsm) != 0 and len(gsm) != 0 and len(letype) != 0 and len(
                motdepasse) != 0

            if not_empty == True:
                for elem in all_douanier_data:
                    old_cin = elem[1]
                    if old_cin == cin:
                        messagebox.showerror("error", 'ce CIN est deja existe dans le system')

                for elem in all_douanier_data:
                    letype = elem[7]
                    if str(letype) == "directeur":
                        admin_pass = elem[8]
                        admin_cin = elem[1]
                        if str(admin_pass) == str(admin_password) and str(admin_cin) == str(admin_user):
                            sql_funcs.insert_into_douanier(data)
                            pass
                        else:
                            messagebox.showerror("error", 'le mot de passe de directeur est incorrect')
            else:
                messagebox.showerror("error", 'il faut de remplir tous la formulaire')
        else:
            messagebox.showerror("error", 'les deux mode de passe ne sont pas similaire')

        return
    logo_btn = ttk.Button(right_frame, width=2, image=logo, command=None).grid(row=0, column=2)
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



    register_btn = Button(right_frame,width=15,text='Register', bg= "#c9c230",font=f,relief=SOLID,cursor='hand2',command=lambda : validateLogin(   register_nummartricule.get(),register_cin.get(),register_nom.get(), register_prenom.get(), register_email.get(),  register_address.get(),  register_gsm.get(),  register_type.get(), register_pwd.get(),pwd_again.get(),adminuser.get(),adminpwd.get()))
    register_btn.grid(row=15, column=2, pady=10, padx=20)

    back_btn = Button(right_frame,width=15,text='back', font=f,relief=SOLID,cursor='hand2',command=lambda : rasie_frame((login_page_frame)))
    back_btn.grid(row=15, column=1, pady=10, padx=20)

def new_contravention(right_frame) :
    def add_new_contravention(refnumbureau_info, datecreation_info, region, procuration_info, proc_cin_original_info,
                              cin_info, nom_info, prenom_info, email_info, address_info, gsm_info):

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

        numseq = str(str(cin) + str(now))
        numseq = numseq.replace(" ", "-")
        numseq = numseq.replace(":", "-")

        not_empty_bool = len(refnumbureau) != 0 and len(datecreation) != 0 and len(regioncreation) != 0 and len(
            procuration) != 0 and len(proc_cin_original) != 0 and len(cin) != 0 and len(nom) != 0 and len(
            prenom) != 0 and len(email) != 0 and len(address) != 0 and len(gsm) != 0 and len(numseq) != 0
        if not_empty_bool:
            all_douaniers = get_random_douanier()

            doaunier1 = all_douaniers[0]
            douanier2 = all_douaniers[1]
            douanier3 = all_douaniers[2]
            douanier4 = all_douaniers[3]

            data_contrevenant = [procuration, proc_cin_original, cin,
                                 nom, prenom, email, address, gsm, numseq]

            data_contravention = [refnumbureau, datecreation, regioncreation,
                                  comment1, comment2, comment3, comment4,
                                  doaunier1, douanier2, douanier3, douanier4,
                                  commentstat1, commentstat2, commentstat3, commentstat4,
                                  numseq]

            sql_funcs.insert_into_contrevenant(data_contrevenant)
            sql_funcs.insert_into_contravention(data_contravention)
        else:
            messagebox.showerror("error", "il fault le remplir tous les champs")
        return 0

    def get_random_douanier():

        directeur_tab = []
        sous_directeur_tab = []
        reviseur_tab = []
        inspecteur_tab = []

        all_douanier = sql_funcs.select_douanier()
        for douanier in all_douanier:

            letype = douanier[7]
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

        return [douanier1, douanier2, douanier3, douanier4]

    logo_btn = ttk.Button(right_frame, width=2, image=logo, command=None).grid(row=0, column=2)

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



    nouv_contra_btn = Button(right_frame,width=15,text='Ajouter',bg= "#c9c230", font=f,relief=SOLID,cursor='hand2',command=lambda : add_new_contravention( refnumbureau_info.get() , datecreation_info.get() ,  region.get() ,  procuration_info.get() , proc_cin_original_info.get(),cin_info.get(),nom_info.get(),prenom_info.get(),email_info.get(),address_info.get(),gsm_info.get()))
    nouv_contra_btn.grid(row=15, column=2, pady=10, padx=20)

    nouv_contra_btn = Button(right_frame,width=15,text='Back', font=f,relief=SOLID,cursor='hand2',command=lambda :rasie_frame(login_page_frame) )
    nouv_contra_btn.grid(row=15, column=1, pady=10, padx=20)


    return 0



##############################################################

#douanier_cntraves = orgnize_douaniers_data(current_doaunier)

###############################################################


root = Tk()
root.title('Douane')
root.iconbitmap(r"logo.ico")

#logo  = PhotoImage(file='logo.png')
image = Image.open(r"logo.png")
resied_image= image.resize((50, 50))
logo = ImageTk.PhotoImage(resied_image)


login_page_frame = Frame(root)

register_page_frame =Frame(root)
main_page_frame =Frame(root)
add_contravention_page_frame =Frame(root)

for frame in (login_page_frame,register_page_frame,main_page_frame,add_contravention_page_frame) :
    frame.grid(row= 0 , column= 0 , sticky= 'news')





#Label(main_page_frame,text="address ",bg='#CCCCCC',font=f).pack()
#nouv_contra_btn = Button(main_page_frame,width=15,text='Ajouter', font=f,relief=SOLID,cursor='hand2',command=lambda : rasie_frame((main_page_frame))).pack()


rasie_frame(login_page_frame)
login_page(login_page_frame)


register_page(register_page_frame)






new_contravention(add_contravention_page_frame)




root.mainloop()

















