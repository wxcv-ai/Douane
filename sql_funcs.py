
import psycopg2
import os



def encode_string(string) :

    return "'"+str(string)+"'"

def select_contravention():
    con = psycopg2.connect(host="127.0.0.1",database="douane",user="postgres",password="admin")

    # cursor
    cur = con.cursor()
    query =    "SELECT * FROM  contravention"
    cur.execute(query)

    query_data = cur.fetchall()

    con.commit()
    cur.close()

    con.close()
    return query_data

def select_contrevenant ():
    con = psycopg2.connect(host="127.0.0.1",database="douane",user="postgres",password="admin")

    # cursor
    cur = con.cursor()
    query =    "SELECT * FROM  contrevenant"
    cur.execute(query)

    query_data = cur.fetchall()

    con.commit()
    cur.close()

    con.close()
    return query_data

def select_douanier():
    con = psycopg2.connect(host="127.0.0.1",database="douane",user="postgres",password="admin")

    # cursor
    cur = con.cursor()
    query =    "SELECT * FROM  douanier"
    cur.execute(query)

    query_data = cur.fetchall()

    con.commit()
    cur.close()

    con.close()
    return query_data


def select_contravention_specific(numseq):
    con = psycopg2.connect(host="127.0.0.1",database="douane",user="postgres",password="admin")

    # cursor
    cur = con.cursor()
    query =    "SELECT * FROM  contravention where numseq = "+encode_string(numseq)
    cur.execute(query)

    query_data = cur.fetchall()

    con.commit()
    cur.close()

    con.close()
    return query_data

def select_contrevenant_specific (numseq):
    con = psycopg2.connect(host="127.0.0.1",database="douane",user="postgres",password="admin")

    # cursor
    cur = con.cursor()
    query =    "SELECT * FROM  contrevenant  where numseq = "+encode_string(numseq)
    cur.execute(query)

    query_data = cur.fetchall()

    con.commit()
    cur.close()

    con.close()
    return query_data


def insert_into_contravention(data):

    con = psycopg2.connect(host="127.0.0.1",database="douane",user="postgres",password="admin")

    #data = [refnumbureau,datecreation,regioncreation,comment1,comment2,comment3,comment4, doaunier1,doaunier2,doaunier3,doaunier4,commentstat1,commentstat2,commentstat3,commentstat4]
    refnumbureau = data[0]
    datecreation= data[1]
    regioncreation= data[2]

    comment1= data[3]
    comment2= data[4]
    comment3= data[5]
    comment4= data[6]

    doaunier1= data[7]
    douanier2= data[8]
    douanier3= data[9]
    douanier4= data[10]

    commentstat1= data[11]
    commentstat2= data[12]
    commentstat3= data[13]
    commentstat4 = data[14]


    num_seq = data[15]

    cur = con.cursor()
    query =    "INSERT INTO contravention (refnumbureau   , datecreation  , regioncreation , comment1  , comment2  , comment3  , comment4  , doaunier1  , douanier2  , douanier3  , douanier4  , commentstat1  ,commentstat2  ,commentstat3  ,commentstat4 ,numseq ) VALUES " \
               "("+\
               encode_string(refnumbureau)+","+encode_string(datecreation)+","+encode_string(regioncreation)+","+encode_string(comment1)+\
               ","+encode_string(comment2)+","+encode_string(comment3)+","+encode_string(comment4)+","+encode_string(doaunier1)+\
               ","+encode_string(douanier2)+","+encode_string(douanier3)+","+encode_string(douanier4)+","+encode_string(commentstat1)+\
               ","+encode_string(commentstat2)+","+encode_string(commentstat3)+","+encode_string(commentstat4)+","+encode_string(num_seq)\
               +")"
    print(query)
    cur.execute(query)

    con.commit()
    cur.close()

    con.close()
    return 0
    #data = [refnumbureau,datecreation,regioncreation,comment1,comment2,comment3,comment4, doaunier1,doaunier2,doaunier3,doaunier4,commentstat1,commentstat2,commentstat3,commentstat4]

data = ["refbureau","datation","regreation","cment1","cment2","cment3","cment4", "doier1","dnier2","dnier3","doer4",True,False,False,False]
#insert_into_contravention(data)
def insert_into_contrevenant(data):

    con = psycopg2.connect(host="127.0.0.1",database="douane",user="postgres",password="admin")
    #data[procuration , proc_cin_original , cin ,nom ,prenom ,email ,address ,gsm ]

    procuration = data[0]
    proc_cin_original= data[1]
    cin= data[2]

    nom= data[3]
    prenom= data[4]
    email= data[5]
    address= data[6]
    gsm= data[7]

    numseq = data[8]


    cur = con.cursor()
    query =    "INSERT INTO contrevenant (procuration   , proc_cin_original  , cin , nom  , prenom  , email  , address  , gsm   , numseq) VALUES " \
               "("+\
               encode_string(procuration)+","+encode_string(proc_cin_original)+","+encode_string(cin)+","+encode_string(nom)+\
               ","+encode_string(prenom)+","+encode_string(email)+","+encode_string(address)+","+encode_string(gsm)+","+encode_string(numseq)\
               +")"
    print(query)
    cur.execute(query)

    con.commit()
    cur.close()

    con.close()
    return 0
    #data = [refnumbureau,datecreation,regioncreation,comment1,comment2,comment3,comment4, doaunier1,doaunier2,doaunier3,doaunier4,commentstat1,commentstat2,commentstat3,commentstat4]

data = [True,"datation","regreation","cment1","cment2","cment3","cment4", "doier1","dnier2","dnier3","doer4",True,False,False,False]

#insert_into_contrevenant(data)

def insert_into_douanier(data):

    con = psycopg2.connect(host="127.0.0.1",database="douane",user="postgres",password="admin")
    #data = [nummartricule ,cin , nom , prenom ,email , address , gsm , letype , motdepasse ]

    nummartricule = data[0]
    cin= data[1]
    nom= data[2]

    prenom= data[3]
    email= data[4]
    address= data[5]
    gsm= data[6]
    letype= data[7]
    motdepasse= data[8]

    cur = con.cursor()
    print("hi")
    query =    "INSERT INTO douanier (nummartricule     , cin , nom  , prenom  , email  , address  , gsm , letype , motdepasse   ) VALUES " \
               "("+\
               encode_string(nummartricule)+","+encode_string(cin)+","+encode_string(nom)+\
               ","+encode_string(prenom)+","+encode_string(email)+","+encode_string(address)+","+encode_string(gsm)+ \
                "," + encode_string(letype) + "," + encode_string(motdepasse)\
               +")"
    print(query)
    cur.execute(query)

    con.commit()
    cur.close()

    con.close()
    return 0
    #data = [refnumbureau,datecreation,regioncreation,comment1,comment2,comment3,comment4, doaunier1,doaunier2,doaunier3,doaunier4,commentstat1,commentstat2,commentstat3,commentstat4]

data = ["nummartricule" ,"cin" , "nom" , "prenom" ,"email" , "address" , "gsm" , "letype" , "motdepasse" ]
#insert_into_douanier(data)

def update_contravention(data):

    con = psycopg2.connect(host="127.0.0.1", database="douane", user="postgres", password="admin")

    # cursor
    comment_name = data[0]
    comment_data = data[1]
    comment_boolean = data[2]
    numseq = data[3]


    cur = con.cursor()

    query = " UPDATE contravention SET "+str(comment_name)+" = "+encode_string(comment_data) +", "+comment_boolean+"="+str(True)+" WHERE numseq = "+encode_string(numseq)
    print(query)
    if len(comment_data)!=0 :
        cur.execute(query)

    con.commit()
    cur.close()

    con.close()
    return 0