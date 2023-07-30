
import mysql.connector as sq
import random
from datetime import date,time,datetime,timedelta
con = sq.connect(host="localhost",user="root",passwd="vineet3012",database="library")
cur = con.cursor()
if con.is_connected():
    print("sucessful")
else:
    print("failed")
#cur.execute("CREATE DATABASE library")
#cur.execute("CREATE TABLE book(name nchar(60),quantity int,realquan int,date DATE,price nchar(10))"
#cur.execute("CREATE TABLE notreturned(name nchar(60),class nchar(5),sec nchar(3),leasedate DATE,returndate DATE)")
#cur.execute("ALTER TABLE notreturned ADD recode nchar(100)")
seting = [1,10,2]
cod = []
def cone(name):
    insert = ("SELECT count(name) FROM student WHERE name=%s and bookreturn=%s")
    value = (name,1)
    cur.execute(insert,value)
    z = cur.fetchall()
    con = [item for t in z for item in  t]
    return(con)
def notreturn():
    ret = date.today() + timedelta(days=-1)
    insert ="SELECT name,class,sec,returndate,recode FROM student WHERE returndate=%s or bookreturn=%s"
    val = (ret,11111)
    cur.execute(insert,val)
    ei = cur.fetchall()
    if len(ei) != 0 :
        print("Name  ,  class  ,  sec  ,returndate")
        for row in ei :
          insert ="INSERT INTO notreturned(name,class,sec,returndate,recode) VALUES(%s,%s,%s,%s,%s)"
          val = (row[0],row[1],row[2],row[3],row[4])
          cur.execute(insert,val)
          print("sucessful")
    else:
        print("nothing")
while True :
 dt = date.today()
 notreturn()
 book = str(input("which book you want:- "))
 boo = book.isnumeric()
 print(boo)
 cur.execute("SELECT name FROM book")
 l= cur.fetchall()
 lib = [item for t in l for item in  t]
 if book == "return" :
     print("enter 1 for take record of today return")
     print("enter 2 for check due of book of previous day ")
     print("enter 3 to see custum date return table ")
     inp = int(input("enter your choice"))
     if inp == 1 :
      insert ="SELECT name,class,sec,returndate FROM student WHERE returndate=%s or class=%s"
      val = (dt,0)
      cur.execute(insert,val)
      e = cur.fetchall()
      if len(e) != 0 :
       print("Name  ,  class  ,  sec  ,returndate")
       for row in e :
          print(row)
      else:
          print("there is no book tom return today")      
     elif inp == 2 :
       insert ="SELECT name,class,sec,returndate,recode FROM student"
       cur.execute(insert)
       p = cur.fetchall()
       print("student who have note sumited and date pass")
       print("Name  ,  class  ,  sec  ,returndate")
       for row in p :
           print(row)
 elif book == "setup":
     print("enter 1 to set up minimum class to borrow book")
     print("enter 2  to set up maximum class to borrow book")
     print("enter 3 to set maximum book to borrow at one time")
     print("enter 5 to see all setting ")
     setu = int(input("enter your choice:- "))
     if setu == 1 :
         setup = int(input("enter minimum class:- "))
         seting[0] = setup
         print("seting changed")
     elif setu == 2 :
         setup = int(input("enter maximum class:- "))
         seting[1] = setup
         print("setting changed")
     elif setu == 3 :
         setup = int(input("borrow limit for a student:- "))
         seting[2] = setup
         print("setting changed")
     elif setu == 4 :
         print("minimum class to borrow book is", seting[0])
         print("maximum class to borrow book",seting[1])
         print("maximum book to borrow at one time",seting[2])
 elif book == "add" :
     na = str(input("please enter book name:- ")).lower()
     qu = int(input("please enter book quantity:- "))
     pr = str(input("enter price charged if book is damaged:- "))
     ch = str(input("are you sure to add this book y or n:- ")).lower()
     if ch == "y" :
         insert = "INSERT INTO book(name,quantity,realquan,date,price) VALUES(%s,%s,%s,%s,%s)"
         val = (na,qu,qu,dt,pr)
         cur.execute(insert,val)
         print("sucessfully added")
     else:
         print("no problem")
 elif book in lib :
      insert = ("SELECT realquan FROM book WHERE name=%s or quantity=%s")
      val = (book,book)
      cur.execute(insert,val)
      n = cur.fetchall()
      nu = [item for t in n for item in t]
      num = nu[0]
      print(num)
      if num > 0:
          co = str(input("yes we have the book in the library do you borrow this book y or n:- ")).lower()
          if co == "y":
              codee = random.randint(1,10000)
              name = str(input("please enter your name:- "))
              clas = int(input("please enter your class:- "))
              sect = str(input("enter your section:- "))
              co = cone(name)
              print(co)
              if co[0] < seting[2] :
               re = int(input("for how many days you want to borrow:- "))  
               retunnn = date.today() + timedelta(days=re)
               if seting[1] >= clas >= seting[0] :
                qua = nu[0] - 1
                inserta = ("INSERT INTO student(name,class,sec,leasedate,returndate,recode,bookname,bookreturn) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)");
                vala = (name,clas,sect,dt,retunnn,codee,book,1)
                cur.execute(inserta,vala)
                insert = ("UPDATE book SET realquan=%s WHERE name=%s ")
                val = (qua,book)
                cur.execute(insert,val)
                print("your return code is:- ",codee)
                print("this code will help in return")

               else :
                  print("You can't take a book from library")
              else:
                print("you cant take more than",co[0],"book from library at a time")

          else :
              print("no problem")
              continue
      else:
          print("sorry this book is taken by someone")
          continue
 
 elif book.strip().isdigit() :
     insert = ("SELECT name,bookname FROM student WHERE recode=%s and bookreturn=%s")
     val = (book,1)
     cur.execute(insert,val)
     e = cur.fetchall()
     ex = [item for t in e for item in  t]
     insert = ("SELECT realquan FROM book WHERE name=%s or quantity=%s")
     val = (ex[1],ex[1])
     cur.execute(insert,val)
     n = cur.fetchall()
     nu = [item for t in n for item in t]
     num = nu[0]
     print(num)
     if len(ex) != 0 :
         print("your name is",ex[0])
         ret = str(input("are you sure to retun this book y or n :- "))
         if ret == "y":
             print("please keep the book on return table")
             numm = num + 1
             insert = ("UPDATE student SET bookreturn=%s,returndate=%s WHERE recode=%s ")
             val = (0,dt,book)
             cur.execute(insert,val)
             insert = ("UPDATE book SET realquan=%s WHERE name=%s ")
             val = (numm,ex[1])
             cur.execute(insert,val)
             insert = "DELETE FROM notreturned WHERE recode=%s or class=%s"
             val=(book,0)
             cur.execute(insert,val)
             print("return sucessful")
     else:
        print("enter the code correct")
        continue
 else :
     print("sorry we dont have the book in the library")
     print("Thank you")
     continue
cur.close()
              
       
 
