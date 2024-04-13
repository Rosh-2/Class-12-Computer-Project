import mysql.connector
from tabulate import tabulate
 
db=input("ENTER NAME OF YOUR DATABASE:")
mydb=mysql.connector.connect(host="localhost",user="root",password='AryaAlan20')
mycursor=mydb.cursor()
 
sql="CREATE DATABASE IF NOT EXISTS %s"%(db)
mycursor.execute(sql)
print("DATABASE CREATED SUCCESSFULLY...")
mycursor=mydb.cursor()
mycursor.execute("USE "+db)
TableName=input("NAME OF YOUR TABLE TO BE CREATED:")
query="CREATE TABLE IF NOT EXISTS "+TableName+"(GCODE int primary key,\
GNAME varchar(20) not null,\
SIZE char(2),\
COLOUR varchar(10),PRICE int)"
print("TABLE "+TableName+" CREATED SUCCESSFULLY...")
mycursor.execute(query)
 
while True:
    print("\n")
    print("-"*80)
    print("\t\t\t\tMain Menu")
    print("-"*80)
    print("\t\t\t1. ADDING GARMENT RECORD")
    print("\t\t\t2. FOR DISPLAYING RECORD OF ALL THE GARMENTS")
    print("\t\t\t3. FOR DISPALYING RECORD OF A PARTICULAR GARMENT")
    print("\t\t\t4. FOR DELETING A RECORD OF A PARTICULAR GARMENT")
    print("\t\t\t5. FOR MODIFICATION IN A RECORD")
    print("\t\t\t6. FOR EXIT")
    print("ENTER CHOICE:",end="")
    choice=int(input())
    if choice==1:
        try:
            print("ENTER GARMENT INFORMATION...")
            mcode=int(input("ENTER GCODE:"))
            mname=input("ENTER GNAME:")
            msize=input("ENTER SIZE:")
            mcolour=input("ENTER COLOUR:")
            mprice=int(input("ENTER PRICE:"))
            rec=(mcode,mname,msize,mcolour,mprice)
            query="insert into "+TableName+" values(%s,%s,%s,%s,%s)"
            mycursor.execute(query,rec)
            mydb.commit()
            print("RECORD ADDED SUCCESSFULLY...")
        except:
             print("SOMETHING WENT WRONG")
 
    elif choice==2:
        try:
            query="select*from "+TableName
            mycursor.execute(query)
            print((tabulate(mycursor,headers=["GCODE","GNAME","SIZE","COLOUR","PRICE"],tablefmt="psql")))
        except:
            print("SOMETING WENT WRONG")
 
    elif choice==3:
        try:
            en=input("ENTER GCODE NUMBER OF THE RECORD TO BE DISPLAYED:")
            query="select*from "+TableName+" where GCODE="+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("\nRECORD OF GARMENT NUMBER:"+en)
            print(myrecord)
            c=mycursor.rowcount
            if c==-1:
                print("NOTHING TO DISPLAY")
        except:
            print("SOMETHING WENT WRONG")
 
    elif choice==4:
        try:
            en=input("ENTER GCODE NUMBER OF THE RECORD TO BE DELECTED:")
            query="delete from "+TableName+" where GCODE="+en
            mycursor.execute(query)
            mydb.commit()
            c=mycursor.rowcount
            if c>0:
                print("DELECTION DONE!!")
            else:
                print("GCODE NUMBER",en,"NOT FOUND")
        except:
            print("SOMETHING WENT WRONG")
 
    elif choice==5:
        try:
            en=input("ENTER GCODE NUMBER OF THE RECORD TO BE MODIFIED:")
            query="select * from "+TableName+" where GCODE="+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==1:
                mname=myrecord[1]
                msize=myrecord[2]
                mprice=myrecord[4]
                print("GCODE   :",myrecord[0])
                print("GNAME   :",myrecord[1])
                print("SIZE    :",myrecord[2])
                print("COLOUR  :",myrecord[3])
                print("PRICE   :",myrecord[4])
                print("--------------------------")
                print("TYPE VALUE TO MODIFY BELOW OR JUST PRESS ENTER FOR NO CHANGE")
                x=input('ENTER GNAME')
                if len(x)>0:
                    mname=x
                x=input("ENTER SIZE")
                if len(x)>0:
                    msize=x
                x=input("ENTER PRICE")
                if len(x)>0:
                    mprice=x
                query='update '+TableName+' set GNAME='+"'"+mname+"'"+','+'SIZE='+"'"+msize+"'"+','+'PRICE='\
                       +str(mprice)+' where GCODE='+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print("RECORD MODIFIED")
            else:
                print('GCODE "+en" DOES NOT EXIST')
        except:
            print("SOMETHING WENT WRONG")
 
    elif choice==6:
        break
    else:
        print("WRONG CHOICE...")
