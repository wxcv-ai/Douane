from tkinter import *
from tkinter import messagebox
import sql_funcs
import pprint

ws = Tk()
ws.title('Enregister Douanier')
ws.config(bg='#0B5A81')

f = ('Times', 12)


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

def get_douanier_contrav(douanier_cin) :

    douanier_data = sql_funcs.select_douanier()

    doaunier_elemnts=[]
    global_douanier_type = ""
    for elem in douanier_data :
        cin = elem[1]
        if str(cin) == str(douanier_cin) :
            letype = elem[7]
            global_douanier_type = letype

    if len(global_douanier_type)!=0 :


        all_data_contravention = sql_funcs.select_contravention()
        for data_contravention in all_data_contravention :
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
                if (str(commentstat4))=="False" and douanier4 == douanier_cin:
                    doaunier_elemnts.append(numseq)
            if global_douanier_type == "sous_directeur":
                if (str(commentstat3))=="False" and douanier3 == douanier_cin:
                    doaunier_elemnts.append(numseq)
            if global_douanier_type == "reviseur":
                if (str(commentstat2))=="False" and douanier2 == douanier_cin:
                    doaunier_elemnts.append(numseq)
            if global_douanier_type == "inspecteur":

                if (str(commentstat1))=="False" and doaunier1 == douanier_cin:
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



    return [refnumbureau ,datecreation ,regioncreation ,comment1 ,comment2 ,comment3 ,comment4 ,doaunier1 ,douanier2 ,douanier3 ,douanier4 ,commentstat1 ,commentstat2 ,commentstat3 ,commentstat4,procuration ,proc_cin_original ,cin ,nom ,prenom ,email ,address ,gsm]

def update_comment(index,current_cin,numseq , data):
    all_douaniers = sql_funcs.select_douanier()
    for douanier in all_douaniers :
        douanier_cin = douanier[1]
        if douanier_cin == current_cin :
            current_type = douanier[7]
    if current_type == "directeur":
        if index == 4 :
            comment_name = "comment4"
            comment_data = data[3]
            comment_boolean = "commentstat4"

            data = [comment_name,comment_data,comment_boolean,numseq]
            sql_funcs.update_contravention(data)
    if current_type == "sous_directeur":
        if index == 3 :
            comment_name = "comment3"
            comment_data = data[2]
            comment_boolean = "commentstat3"
            data = [comment_name,comment_data,comment_boolean,numseq]
            sql_funcs.update_contravention(data)
    if current_type == "reviseur":
        if index == 2 :
            comment_name = "comment2"
            comment_data = data[1]
            comment_boolean ="commentstat2"

            data = [comment_name,comment_data,comment_boolean,numseq]
            sql_funcs.update_contravention(data)
    if current_type == "inspecteur":
        if index == 1 :
            comment_name = "comment1"
            comment_data = data[0]
            comment_boolean = "commentstat1"

            data = [comment_name,comment_data,comment_boolean,numseq]
            sql_funcs.update_contravention(data)
    return 0

def orgnize_douaniers_data(current_doaunier):
    douanier_cntraves = get_douanier_contrav(current_doaunier)

    if len(douanier_cntraves)  > 3 :
        douanier_cntraves = douanier_cntraves[0:2]
    elif len(douanier_cntraves)  == 3 :
        pass
    else :
        num = 3-len(douanier_cntraves)
        for i in range(0,num):
            douanier_cntraves.append(0)
    return douanier_cntraves


current_doaunier = "456"
douanier_cntraves = orgnize_douaniers_data(current_doaunier)

right_frame = Frame(ws, bd=2, bg='#CCCCCC', relief=SOLID)
right_frame.pack()


def upper_buttons():



    Label(right_frame, text=determiner_le_role(current_doaunier), bg='#CCCCCC', font=f).grid(row=0, column=3, sticky=W, pady=10)

    logout_btn = Button(right_frame,width=15,text='log out', font=f,relief=SOLID,cursor='hand2',command=None)
    logout_btn.grid(row=0, column=1, pady=10, padx=20)
    ajouter_contravention = Button(right_frame,width=15,text='ajouter contravention', font=f,relief=SOLID,cursor='hand2',command=None)
    ajouter_contravention.grid(row=0, column=2, pady=10, padx=20)
    return 0

def main_page(i,right_frame):

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

        #numseq = data_contravention[15]

        data_contrevenant = sql_funcs.select_contrevenant_specific(numseq)[0]

        procuration = data_contrevenant[0]
        proc_cin_original = data_contrevenant[1]
        cin = data_contrevenant[2]
        nom = data_contrevenant[3]
        prenom = data_contrevenant[4]
        email = data_contrevenant[5]
        address = data_contrevenant[6]
        gsm = data_contrevenant[7]
        #numseq = data_contrevenant[8]

        Label(right_frame, text="nom prenom:", bg='#CCCCCC', font=f).grid(row=i*6+3, column=0, sticky=W, pady=10)
        Label(right_frame, text=nom +str("")+ prenom, bg='#CCCCCC', font=f).grid(row=i*6+3, column=1, sticky=W, pady=10)

        Label(right_frame,text="cin est:",bg='#CCCCCC',font=f).grid(row=i*6+4, column=0, sticky=W, pady=10)
        Label(right_frame,text=cin,bg='#CCCCCC',font=f).grid(row=i*6+4, column=1, sticky=W, pady=10)

        Label(right_frame,text="TEL:",bg='#CCCCCC',font=f).grid(row=i*6+5, column=0, sticky=W, pady=10)
        Label(right_frame,text=gsm,bg='#CCCCCC',font=f).grid(row=i*6+5, column=1, sticky=W, pady=10)

        Label(right_frame,text="procuraton:",bg='#CCCCCC',font=f).grid(row=i*6+6, column=0, sticky=W, pady=10)
        Label(right_frame,text=procuration,bg='#CCCCCC',font=f).grid(row=i*6+6, column=1, sticky=W, pady=10)


        Label(right_frame,text="cin original de:",bg='#CCCCCC',font=f).grid(row=i*6+3, column=2, sticky=W, pady=10)
        Label(right_frame,text=proc_cin_original,bg='#CCCCCC',font=f).grid(row=i*6+3, column=3, sticky=W, pady=10)


        Label(right_frame,text="date de creation:",bg='#CCCCCC',font=f).grid(row=i*6+4, column=2, sticky=W, pady=10)
        Label(right_frame,text=datecreation,bg='#CCCCCC',font=f).grid(row=i*6+4, column=3, sticky=W, pady=10)


        Label(right_frame,text="numero de bureau:",bg='#CCCCCC',font=f).grid(row=i*6+5, column=2, sticky=W, pady=10)
        Label(right_frame,text=refnumbureau,bg='#CCCCCC',font=f).grid(row=i*6+5, column=3, sticky=W, pady=10)

        Label(right_frame,text="region de creation:",bg='#CCCCCC',font=f).grid(row=i*6+6, column=2, sticky=W, pady=10)
        Label(right_frame,text=regioncreation,bg='#CCCCCC',font=f).grid(row=i*6+6, column=3, sticky=W, pady=10)





        Label(right_frame,text="commentaire 1:",bg='#CCCCCC',font=f).grid(row=i*6+3, column=4, sticky=W, pady=10)
        comm1_input = Entry(right_frame, font=f)
        comm1_input.grid(row=i*6+3, column=5, pady=10, padx=20)
        send_btn = Button(right_frame, width=5, text='Send', font=f, relief=SOLID, cursor='hand2',command=lambda:update_comment(1,current_doaunier,numseq , [comm1_input.get(),comm2_input.get(),comm3_input.get(),comm4_input.get()]))
        send_btn.grid(row=i*6+3, column=6, pady=10, padx=20)

        Label(right_frame,text="commentaire 2:",bg='#CCCCCC',font=f).grid(row=i*6+4, column=4, sticky=W, pady=10)
        comm2_input = Entry(right_frame, font=f)
        comm2_input.grid(row=i*6+4, column=5, pady=10, padx=20)
        send_btn = Button(right_frame, width=5, text='Send', font=f, relief=SOLID, cursor='hand2',command=lambda: update_comment(2,current_doaunier,numseq, [comm1_input.get(),comm2_input.get(),comm3_input.get(),comm4_input.get()]))
        send_btn.grid(row=i*6+4, column=6, pady=10, padx=20)

        Label(right_frame,text="commentaire 3:",bg='#CCCCCC',font=f).grid(row=i*6+5, column=4, sticky=W, pady=10)
        comm3_input = Entry(right_frame, font=f)
        comm3_input.grid(row=i*6+5, column=5, pady=10, padx=20)
        send_btn = Button(right_frame, width=5, text='Send', font=f, relief=SOLID, cursor='hand2',command=lambda:update_comment(3,current_doaunier,numseq, [comm1_input.get(),comm2_input.get(),comm3_input.get(),comm4_input.get()]))
        send_btn.grid(row=i*6+5, column=6, pady=10, padx=20)

        Label(right_frame,text="commentaire 4:",bg='#CCCCCC',font=f).grid(row=i*6+6, column=4, sticky=W, pady=10)
        comm4_input = Entry(right_frame, font=f)
        comm4_input.grid(row=i*6+6, column=5, pady=10, padx=20)
        send_btn = Button(right_frame, width=5, text='Send', font=f, relief=SOLID, cursor='hand2',command=lambda: update_comment(4,current_doaunier,numseq, [comm1_input.get(),comm2_input.get(),comm3_input.get(),comm4_input.get()]))
        send_btn.grid(row=i*6+6, column=6, pady=10, padx=20)


upper_buttons()
main_page(0,right_frame)
main_page(1,right_frame)
main_page(2,right_frame)
ws.mainloop()


