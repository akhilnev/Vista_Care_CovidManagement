#SOURCE CODE
#AKHILESH NEVATIA 
print("*******************************************************************")
print("                                                                   ")
print("            WELCOME TO  THE  HOSPITAL                              ")
print("                                                                   ")
print("                                                                   ")
print("*******************************************************************")

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS covid_management")
mycursor.execute("use covid_management")
mycursor.execute("CREATE TABLE IF NOT EXISTS staff(sno VARCHAR(10),name varchar(25), age int, gender VARCHAR(20),post VARCHAR(25), salary int)")
mycursor.execute("CREATE TABLE IF NOT EXISTS patient(sno VARCHAR(10) , name VARCHAR(20), age int, gender VARCHAR(20), date DATE )")
mycursor.execute("CREATE TABLE IF NOT EXISTS login(admin VARCHAR(25) NOT NULL, password VARCHAR (25) )")
mycursor.execute("CREATE TABLE IF NOT EXISTS sno(patient VARCHAR(25) NOT NULL , staff VARCHAR(25) NOT NULL)")
mycursor.execute("SELECT * FROM SNO")
z=0
for i in mycursor:#[]TO MAKE SURE QUERY IS EXECUTED ONLY ONCE 
    z=1

    if z==0:
        mycursor.execute("insert into sno values('0','0')")
        mydb.commit()
        j=0
        mycursor.execute("select * from login")

        for i in mycursor:
            j=1
        if j==0:
            mycursor.execute("insert into login values('ADMIN','NG')")
            mydb.commit()
    loop1="y"
    while(loop1=="y" or loop1=="Y"):
        print("___________________")
        print("1.Admin")
        print("2.Patient")
        print("3.Exit")
        print("___________________")
        ch1=int(input("ENTER YOUR CHOICE:"))
        if ch1==1:
            pas=input("Enter your password:")
            mycursor.execute("SELECT * FROM LOGIN")
            for i in mycursor:
                username,password=i
            if pas==password:
                loop2='n'
                while(loop2=="n" or loop2=="N"):
                    print("_______________________")
                    print("1.Add patient")
                    print("2. ADD STAFF")
                    print("3. Display Patient Record")
                    print("4. Display Staff Record")
                    print("5. Change password")
                    print("6. Remove patients")
                    print("7. Remove Staff")
                    print("8. Logout")
                    print("_______________________")
                    ch2=int(input("ENTER YOUR CHOICE"))
                    if ch2==1:
                        loop3='y'
                        while (loop3=='y' or loop3=="Y"):
                            name=input("Enter patient name: ")
                            age=input("Enter patients age: ")
                            gender=input("ENTER GENDER: ")
                            date=input("ENTER DATE COVID TEST CAME POSITIVE: ")
                            mycursor.execute("SELECT * FROM SNO")
                            for i in mycursor:
                                patient,staff=i
                                patient=int(patient)+1#to inc patient value in table
                            mycursor.execute("insert into patient values('"+str(patient)+"','"+name+"','"+age+"','"+gender+"','"+date+"')")
                            mycursor.execute("update sno set patient={}".format(str(patient)))
                            mydb.commit()
                            print("DATA OF PATIENT HAS BEEN SAVED SUCCESFULLY")
                            mycursor.execute("select * from patient ")
                            t=0
                            for i in mycursor:
                                t+=1
                                t_id1,name1,age1,gender1,date1=i
                            print(f"Total number of Corona infected patients---->{patient}")
                            print(f"Total active Corona cases----->{t}")
                            print(f"This patient with id ",t_id1," will be in quarintine")
                            loop3=input("DO YOU WANT TO ENTER MORE DATA OF PATIENTS(y/n)")
                        loop2=input("DO YOU WANT TO LOGOUT(y/n)")
                    elif ch2==2:
                        loop3='y'
                        while loop3=='y' or loop3=='Y':
                            name=input("enter staff name:   ")
                            age=input("enter age:   ")
                            gender=input("enter gender(m/f):    ")
                            post=input("enter his/her post:   ")
                            salary=input("enter his/her salary:    ")

                            mycursor.execute("select * from sno")
                            for i in mycursor:
                                patient,staff=i
                                staff=int(staff)+1
                            mycursor.execute("insert into staff values('"+str(staff)+"','"+name+"','"+age+"','"+gender+"','"+post+"','"+salary+"')")
                            mycursor.execute("update sno set staff='"+str(staff)+"'")
                            mydb.commit()
                            print(f"staff with id {staff} has been saved succesfully.....")
                            mycursor.execute("select* from staff")
                            t=0
                            for i in mycursor:
                                t+=1

                            print(f"activate staff members--- {t}")
                            loop3=input("do u want to enter more staff data(y/n):  ")
                        loop2=input("do u want to logout(y/n):    ")
                    elif ch2==3:
                        idd=input("enter patient's ID:   ")#id must exist
                        mycursor.execute("select * from patient where sno='"+idd+"'")
                        t_id2,name2,age2,gender2,date2=["","","","",""]
                        for i in mycursor:
                            t_id2,name2,age2,gender2,date2=i
                        print(f"| id | name | age | gender | corona positive date |")
                        print(f"| {t_id2} | {name2} | {age2} | {gender2} | {date2} |")
                    elif ch2==4:
                        idd=input("enter staff id:  ")#id is self generated in option 2
                        t_id3,name3,age3,gender3,post3,salary3=["","","","","",""]
                        mydb.commit()
                        mycursor.execute("select * from staff where sno='"+idd+"'")
                        for i in mycursor:
                            t_id3,name3,age3,gender3,post3,salary3=i
                        print("| id | name | age | gender | post | salary |")
                        print(f"| {t_id3} | {name3} | {age3} | {gender3} | {post3} | {salary3} |")
                    elif ch2==5:
                        pas=input("enter old password:   ")
                        mycursor.execute("select * from login")
                        for i in mycursor:
                            username,password=i
                        if pas==password:
                            npas=input("enter new password:   ")
                            mycursor.execute("update login set password='"+npas+"'")
                            mydb.commit()
                        
                    elif ch2==6:
                        loop3='y'
                        while loop3=='y' or loop3=='Y':
                            idd=input("enter patient id")
                            mycursor.execute("delete from patient where sno='"+idd+"'")
                            mydb.commit()
                            print("patient has been removed succesfully")
                            loop3=input("do you want to remove more patients(y/n):   ")
                    elif ch2==7:
                        loop3='y'
                        while loop3=='y' or loop3=='Y':
                            idd=input("enter staff id")
                            mycursor.execute("delete from staff where sno='"+idd+"'")
                            mydb.commit()
                            print("staff has been removed sucessfully")
                            loop3=input("do u want to remove more staff(y/n):   ")
                    elif ch2==8:
                        break
            else:
                print("wrong password,choose option again")
        elif ch1==2:
            print("welcome to the covid test,please answer the follwoing questions")
            icough=input("do you have cough?(y/n):   ").lower()
            dry_cough='n'
            cough='n'
            if icough=='y' or icough=='Y':
                dry_cough=input("is the cough dry(y/n):   ").lower()
                cough=input("is the cough wet(y/n):   ").lower()

            sneeze=input("do you sneeze often?(y/n):   ").lower()
            pain=input("do you have body pain?(y/n):    ").lower()
            weakness=input("do you feel weak?(y/n):    ").lower()
            mucus=input("do your nose/lungs have mucus?(y/n):   ").lower()
            itemp=int(input("enter body temp:  "))
            if itemp<=100:
                temp='low'
            else:
                temp='high'
            breath=input("are you having difficulty breathing?(y/n):   ")
            if(dry_cough=='y' and sneeze=='y' and pain=='y' and weakness=='y'and temp=='high' and breath=='y'):
                print("sorry according to this test you have a high posibility of having corona,please get a swab test done")
                name=input("enter your name:  ")
                age=input("enter age:  ")
                gender=input("enter your gender(m/f):  ")
                mycursor.execute("select * from sno")
                for i in mycursor:
                    patient,staff=i
                    patient=int(patient)+1
                mycursor.execute("insert into patient values('"+str(patient)+"','"+name+"','"+age+"','"+gender+"',now())")
                mydb.commit()
                print("data of patient has been saved sycessfully")
                print("total number of corona infected patients-- {patient}")
                mycursor.execute("select * from patients")
                t=0
                for i in mycursor:
                    t+=1
                print(f"active corona cases--- {t}")
                mycursor.execute("select * from patient")
                for i in mycursor:
                    t_id5,name5,age5,gender5,date5=i
                print(f"this patient with id {t_id5} will be in quarantine upto 14 days from{date5}")
            elif(dry_cough=='y' and sneeze=='y' and pain=='n' and weakness=='n' and temp=='low' and breadth=='n'):
                print("nothing to wory,you most likely have common cold")
            else:
                print("you are not corona affected, you might have any other flu or disease ; if the symptoms increase get a swab test done to be on the safer side;PLEASE CONSULT YOUR DOCTOR")
        elif ch1==3:
            break
