# import mysql.connector as mysql
# myobj=mysql.connect("localmhost","root","")
# cursorobj=myobj.cursor()
# try:
#   db="create database school"
#   cursorobj.execute(db)
#   print("database created")
# except:
#     print("database error")
# from getpass import getpass

# create database -----------------------------------------

# import mysql as mysql

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )
# cursorobj=mydb.cursor()
# try:
#  db="create database school"
#  cursorobj.execute(db)
#  print("created")

# except:
#     print("error")

# connect database create table----------

import mysql.connector as mysql

# mydb = mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="school"  )  # connect database that already created

# mysqlc=mydb.cursor()
# try:
#  tc="CREATE TABLE studentdata(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), rollno VARCHAR(20), branch VARCHAR(20), address VARCHAR(12))"
#  mysqlc.execute(tc)
#  print("database created")
# except:
#   print("database already exists")

# incert data in the table--------------------------------------------------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="school"  )
# mysqlc=mydb.cursor()
# try:
#  itd="INSERT INTO studentdata(name,rollno,branch,address) values(%s,%s,%s,%s)"
# #  i=("tanmay","121212","cs","meerut")
# # add many values in one list
#  i=[("tanmay","121212","ai","meerut"),("Amit","3442","ec","meerut"),("Akash","54657","cs","meerut"),("nikhil","65734","ec","meerut"),("uday","765756","cs","meerut"),("rahul","75645","ml","meerut")]
# #  mysqlc.execute(itd,i)
# # if add many values in one list
#  mysqlc.executemany(itd,i)
#  mydb.commit()
# #  print("data is inserted")
# except:
#   print("error")

# if add many list create tuples in the list
#  i=[("tanmay","121212","ai","meerut"),("Amit","3442","ec","meerut"),("Akash","54657","cs","meerut"),("nikhil","65734","ec","meerut"),("uday","765756","cs","meerut"),("rahul","75645","ml","meerut")]
# use executemany for multiple values
#  mysqlc.executemany(itd,i)


# create databse with custom details
# mydb=mysql.connect(
#     host="localhost",
#     user="root",
#     passwd=""

# )
# mysqlc=mydb.cursor()
# try:
#   db="CREATE DATABASE student_data"
#   mysqlc.execute(db)
#   print("created")
# except:
#     print("error")
# connect amd create table and insert data
# mydb=mysql.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="student_data"
# )
# mysqlc=mydb.cursor()
# try:
#  db="CREATE TABLE student(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(23), email VARCHAR(50))"
#  mysqlc.execute(db)
#  print("table is created",db)
# except:
#     print("error is raised ")
# insert into
# mydb=mysql.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="student_data"
# )
# mysqlc=mydb.cursor()
# try:
#     db="INSERT INTO student(name,email) values(%s,%s)"
#     i=[("tanmay","tanmay@gmail.com"),("tanmay","tanmay@gmail.com"),("tanmay","tanmay@gmail.com"),("tanmay","tanmay@gmail.com")]
#     mysqlc.executemany(db,i)
#     mydb.commit()
#     # print("insert complete")
# except:
#     print("error ")


# selection queury in python sql------------------------------------------------------


# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="school"  )
# mysqlc=mydb.cursor()
# # print("{:^20}{:<30}{:<15}{:<20}{:<20}".format("id","name","rollno","branch","address"))
# print("{:^20}{:<30}{:<30}".format("id","name","rollno"))

# try:
#     # mysqlc.execute(" SELECT*FROM studentdata ")  # select query
#     mysqlc.execute(" SELECT * FROM studentdata ")    # display limited items . specific
#     myresult=mysqlc.fetchall()
#     for x in myresult:
#         # print("{:^20}{:<30}{:<15}{:<20}{:<20}".format(x[0],x[1],x[2],x[3],x[4]))
#          print("{:^20}{:<30}{:<15}".format(x[0],x[1],x[2]))

# except:
#     print("error")

# display single row

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="school"  )
# mysqlc=mydb.cursor()
# # print("{:^20}{:<30}{:<15}{:<20}{:<20}".format("id","name","rollno","branch","address"))
# print("{:^20}{:<30}{:<30}".format("id","name","rollno"))

# try:
#     # mysqlc.execute(" SELECT*FROM studentdata ")  # select query
#     mysqlc.execute(" SELECT * FROM studentdata where id=12")    # display limited items . specific
#     myresult=mysqlc.fetchone()
#     # for x in myresult:
#         # print("{:^20}{:<30}{:<15}{:<20}{:<20}".format(x[0],x[1],x[2],x[3],x[4]))
#     print("{:^20}{:<30}{:<15}".format(myresult[0],myresult[1],myresult[2]))

# except:
#     print("error")


# delete query -------------------------------------------------------------------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="school"  )
# mysqlc=mydb.cursor()
# # inp=int(input("enter the id : "))
# sql=" DELETE FROM studentdata WHERE id = 11"
# try:
#  mysqlc.execute(sql)
#  mydb.commit()
#  print("item is deleted")
# except:
#     print("error")


# update query ------------------------------------------------------------------------

# with user input update

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="school"  )
# mysqlc=mydb.cursor()
# inp_id=int(input("enter the id : "))
# name=str(input("enter the name : "))
# branch=str(input("enter the branch : "))
# sql=" UPDATE studentdata SET name=%s,branch=%s WHERE id = %s"
# # data=("tanmay","ML",inp)
# data=(name,branch,inp_id)
# try:
#     mysqlc.execute(sql,data)
#     mydb.commit()
#     print("data updated")
# except:
#     print("error")

# without input direct update

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="school"  )
# mysqlc=mydb.cursor()
# sql=" UPDATE studentdata SET name=%s,branch=%s WHERE id = 12"
# data=("tanmay","ML")
# try:
#     mysqlc.execute(sql,data)
#     mydb.commit()
#     print("data updated")
# except:
#     print("error")

# order by or set limit on the data --------------------------------------------------------------------------


# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="school"  )
# mysqlc=mydb.cursor()
# print("{:^20}{:<30}{:<30}{:<30}".format("id","name","branch","address"))
# try:
#   # order by DESC: decending order
#   # ACE: acanding order
#   # limit (position,no of data)
#   # ex: (2,3) 2 says that data will be show above value 2 and 3 says no of data show will be 3 after 2nd position
#   sql=" SELECT * FROM studentdata ORDER BY id DESC LIMIT 1,3"
#   mysqlc.execute(sql)
#   myresult=mysqlc.fetchall()
#   for x in myresult:
#     print("{:^20}{:<30}{:<30}{:<30}".format(x[0],x[1],x[2],x[3]))
# except:
#   print("error")

# searching and filter data query ----------------------------------------------------------

# searching-------------------------------------------------------------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="school"  )
# mysqlc=mydb.cursor()
# print("{:^20}{:<30}{:<30}{:<30}".format("id","name","branch","address"))
# try:
#   inp_name=input("enter the data do you want to search: ")
#   sql=" SELECT * FROM studentdata WHERE name like '%"+inp_name+"%'"
#   mysqlc.execute(sql)
#   myresult=mysqlc.fetchall()
#   for x in myresult:
#     print("{:^20}{:<30}{:<30}{:<30}".format(x[0],x[1],x[2],x[3]))
# except:
#   print("error")

# filter-----------------------------------------------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="school"  )
# mysqlc=mydb.cursor()
# print("{:^20}{:<30}{:<20}{:<30}{:<30}".format("id","name","rollno","branch","address"))
# try:
#   inp_name=input("enter the data do you want to search: ")
#   inp_branch=input("enter the branch: ")
#   # and----
#   sql=" SELECT * FROM studentdata WHERE name ='"+inp_name+"' and branch = '"+inp_branch+"' "
#   # or -----
#   # sql=" SELECT * FROM studentdata WHERE name ='"+inp_name+"' or branch = '"+inp_branch+"' "
#   mysqlc.execute(sql)
#   myresult=mysqlc.fetchall()
#   for x in myresult:
#     print("{:^20}{:<30}{:<20}{:<30}{:<30}".format(x[0],x[1],x[2],x[3],x[4]))
# except:
#   print("error")

# join-------------------------------------------------------

# create database-------------------------------------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd=""
# )
# mysqlc=mydb.cursor()
# try:
#  db=" CREATE DATABASE data"
#  mysqlc.execute(db)
#  print("database created ")
# except:
#   print("error")

# create table-----------------------------------------------

# create state table ----------------------------------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
# )
# mysqlc=mydb.cursor()
# try:
#  tc="CREATE TABLE state ( state_id INT AUTO_INCREMENT PRIMARY KEY , state_name VARCHAR(20) , country_id INT )"
#  mysqlc.execute(tc)
#  print("table created ")
# except:
#   print("error")

# create country table ---------------------------------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
# )
# mysqlc=mydb.cursor()
# try:
#  tc=" CREATE TABLE country ( country_id INT , country_name VARCHAR(20) )"
#  mysqlc.execute(tc)
#  print("table created ")
# except:
#   print("error")

# insert data in the table ------------------------------------

# state table-------------
# while True:
#  mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
#  )
#  mysqlc=mydb.cursor()
#  name=input("enter the name : ")
#  count_id=int(input("enter the id : "))

#  try:
#   insert=(" INSERT INTO state ( state_name , country_id ) values(%s,%s)")
#   data=(name,count_id)
#   mysqlc.execute(insert,data)
#   mydb.commit()
#   print("data is created")
#  except:
#   print("error")

# country table----------------------

# while True:
#  mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
#  )
#  mysqlc=mydb.cursor()
#  name=input("enter the name : ")
#  count_id=int(input("enter the id : "))

#  try:
#   insert=(" INSERT INTO country( country_name , country_id ) values(%s,%s)")
#   data=(name,count_id)
#   mysqlc.execute(insert,data)
#   mydb.commit()
#   print("data is created")
#  except:
#   print("error")

# inner join--------------------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
# )
# mysqlc=mydb.cursor()
# print("{:^20}{:<20}{:<20}".format("state_id","state_name","country_name"))
# try:
#   # sql=" SELECT * FROM state INNER JOIN country on state.country_id=country.country_id"
#   # or
#   sql=" SELECT state.state_id,state.state_name,country.country_name FROM state INNER JOIN country on state.country_id=country.country_id"

#   mysqlc.execute(sql)
#   myresult=mysqlc.fetchall()
#   for x in myresult:
#   #  print(x)
#    print("{:^20}{:<20}{:<20}".format(x[0],x[1],x[2]))
# except:
#   print("error")

 # left join---------------------------------------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
# )
# mysqlc=mydb.cursor()
# print("{:^20}{:<20}{:<20}".format("state_id","state_name","country_name"))
# try:
#   # sql=" SELECT * FROM state INNER JOIN country on state.country_id=country.country_id"
#   # or
#  sql=" SELECT state.state_id,state.state_name,country.country_name FROM state LEFT JOIN country on state.country_id=country.country_id"

#  mysqlc.execute(sql)
#  myresult=mysqlc.fetchall()
#  for x in myresult:
#   #  print(x)
#    print("{:^20}{:<20}{:<20}".format(x[0],x[1],str(x[2])))
# except:
#   print("error")

# right join -------------------------------------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
# )
# mysqlc=mydb.cursor()
# print("{:^20}{:<20}{:<20}".format("state_id","state_name","country_name"))
# try:
#   # sql=" SELECT * FROM state,country WHERE state.country_id=country.country_id"
#   # or
#   sql=" SELECT state.state_id,state.state_name,country.country_name FROM state RIGHT JOIN country on state.country_id=country.country_id"
#   mysqlc.execute(sql)
#   myresult=mysqlc.fetchall()
#   for x in myresult:
#     #  print(x)
#     print("{:^20}{:<20}{:<20}".format(x[0],x[1],x[2]))
#     #  print("{:^20}{:<20}{:<20}".format(x[0],x[1],x[4]))

# except:
#   print("error")

# EQUI join------------------------------------------------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
# )
# mysqlc=mydb.cursor()
# print("{:^20}{:<20}{:<20}".format("state_id","state_name","country_name"))
# try:
#   # sql=" SELECT * FROM state,country WHERE state.country_id=country.country_id"
#   sql=" SELECT state.state_id, state.state_name,country.country_name FROM state,country WHERE state.country_id=country.country_id"
#   mysqlc.execute(sql)
#   myresult=mysqlc.fetchall()
#   for x in myresult:
#     #  print(x)
#     print("{:^20}{:<20}{:<20}".format(x[0],x[1],x[2]))
#     #  print("{:^20}{:<20}{:<20}".format(x[0],x[1],x[4]))

# except:
#   print("error")

# self join---------------------------------------------------------

# create database -------------------------------

# mydb=mysql.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="data"
# )
# mysqlc=mydb.cursor()
# sql=" CREATE TABLE category ( cat_id INT PRIMARY KEY , name VARCHAR(20) , parent_id INT )"
# mysqlc.execute(sql)
# mydb.commit()

# insert data---------------------------------
# while True:
#  mydb=mysql.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="data"
#  )
#  mysqlc=mydb.cursor()
#  cat_id=int(input("enter the category id: "))
#  cat_name=input("enter the category name: ")
#  parent_id=int(input("enter the parent_id: "))

#  sql=" INSERT INTO category ( cat_id , name , parent_id ) values(%s,%s,%s)"
#  data=(cat_id,cat_name,parent_id)
#  mysqlc.execute(sql,data)
#  mydb.commit()

# self join---------------------


# mydb=mysql.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="data"
# )
# mysqlc=mydb.cursor()
# sql=" SELECT * FROM category as c1, category as c2 WHERE c1.cat_id=c2.parent_id "
# mysqlc.execute(sql)
# myresult=mysqlc.fetchall()
# for x in myresult:
# #   print(myresult)
#     print(x[1],x[4])

# between operator ---------------------------------------------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
# )
# mysqlc=mydb.cursor()
# print("{:^20}{:<20}{:<20}".format("state_id","state_name","country_name"))
# try:
#   # sql=" SELECT * FROM state INNER JOIN country on state.country_id=country.country_id"
#   # or
#   sql=" SELECT * FROM state WHERE state_id BETWEEN 13 and 15 "

#   mysqlc.execute(sql)
#   myresult=mysqlc.fetchall()
#   for x in myresult:
#   #  print(x)
#    print("{:^20}{:<20}{:<20}".format(x[0],x[1],x[2]))
# except:
#   print("error")

# min() and max() function ------------------------------------------

# min() and max()----------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
# )
# mysqlc=mydb.cursor()
# print("{:^20}{:<20}{:<20}".format("state_id","state_name","country_id"))
# try:
#   # or
# #   sql=" SELECT max(state_id), state_name , max(country_id) FROM state  "
#   sql=" SELECT min(state_id), state_name , min(country_id) FROM state  "


#   mysqlc.execute(sql)
#   myresult=mysqlc.fetchall()
#   for x in myresult:
# #    print(x)
#    print("{:^20}{:<20}{:<20}".format(x[0],x[1],x[2]))
# except:
#   print("error")

# group by : used for grouping the data means that which data how much time are repeating ..----------------------------------

# it show the count of repeated data . similar to the destinct ------------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
# )
# mysqlc=mydb.cursor()
# print("{:^20}{:<20}".format("count","state_name"))
# try:
#   # or
# #   sql=" SELECT max(state_id), state_name , max(country_id) FROM state  "
#   sql=" SELECT count(*),state_name FROM state GROUP BY state_name"


#   mysqlc.execute(sql)
#   myresult=mysqlc.fetchall()
#   for x in myresult:
# #    print(x)
#    print("{:^20}{:<20}".format(x[0],x[1]))
# except:
#   print("error")

# distinct function ------------------------------------------------------------------
# distinct doesn't display repeated data it use the repeated data only one time -------

# DICTINCT()
# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
# )
# mysqlc=mydb.cursor()
# print("{:^20}".format("state_name"))
# try:
#   # or
# #   sql=" SELECT max(state_id), state_name , max(country_id) FROM state  "
#   sql=" SELECT DISTINCT(state_name) FROM state "


#   mysqlc.execute(sql)
#   myresult=mysqlc.fetchall()
#   for x in myresult:
# #    print(x)
#    print("{:<20}".format(x[0]))
# except:
#   print("error")

# sum function ------------------------------
# it display the sum of total data -----------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
# )
# mysqlc=mydb.cursor()
# print("{:^20}".format("state_id"))
# try:
#   sql=" SELECT SUM(state_id) FROM state "



#   mysqlc.execute(sql)
#   myresult=mysqlc.fetchall()
#   # without loop-----------
#   # myresult=mysqlc.fetchone()

#   for x in myresult:
# #    print(x)
#    print("{:^20}".format(x[0]))
#   # without loop --------------
#   #  print("{:^20}".format(myresult[0]))
# except:
#   print("error")

# AVG FUNCTION ---------------
# display the average data of the column-----

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
# )
# mysqlc=mydb.cursor()
# print("{:^20}".format("state_id"))
# try:
#   sql=" SELECT AVG(state_id) FROM state "



#   mysqlc.execute(sql)
#   myresult=mysqlc.fetchall()
#   # without loop-----------
#   # myresult=mysqlc.fetchone()

#   for x in myresult:
# #    print(x)
#    print("{:^20}".format(x[0]))
#   #  without loop --------------
#   #  print("{:^20}".format(myresult[0]))
# except:
#   print("error")

# COUNT() function -------------------
# display the total no of rows in the table----------

# mydb=mysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="data"
# )
# mysqlc=mydb.cursor()
# print("{:^20}".format("state_id"))
# try:
#   # DISPLAY TOTAL NO OF ROWS IN state_id column----------
#   sql=" SELECT  COUNT(state_id) FROM state "

#   # DISLAY TOTAL NO OF ROWS IN THE TABLE -------------
#   sql=" SELECT  COUNT(*) FROM state "




#   mysqlc.execute(sql)
#   myresult=mysqlc.fetchall()
#   # without loop-----------
#   # myresult=mysqlc.fetchone()

#   for x in myresult:
# #    print(x)
#    print("{:^20}".format(x[0]))
#   #  without loop --------------
#   #  print("{:^20}".format(myresult[0]))
# except:
#   print("error")

# IN() AND NOT IN() ----------------------

# IN() it display only condition data , that data we want to display ex(1,2) : it display only 1 and 2 rows data -----------------

mydb=mysql.connect(
  host="localhost",
  user="root",
  passwd="",
  database="data"
)
mysqlc=mydb.cursor()
print("{:^20}{:^20}{:^20}".format("state_id","state_name","country_id"))
try:
  sql=" SELECT * FROM state WHERE state_id IN(12,18) "
  mysqlc.execute(sql)
  myresult=mysqlc.fetchall()
  for x in myresult:
#    print(x)
   print("{:^20}{:^20}{:^20}".format(x[0],x[1],x[2]))

except:
  print("error")

# NOT IN(): it does not display the data that we define in NOT IN() ex: NOT IN (1,3) : it does not dispkay 12 and 13 data . display remaining data ----------

mydb=mysql.connect(
  host="localhost",
  user="root",
  passwd="",
  database="data"
)
mysqlc=mydb.cursor()
print("{:^20}{:^20}{:^20}".format("state_id","state_name","country_id"))
try:
  sql=" SELECT * FROM state WHERE state_id NOT IN(12,18) "
  mysqlc.execute(sql)
  myresult=mysqlc.fetchall()
  for x in myresult:
#    print(x)
   print("{:^20}{:^20}{:^20}".format(x[0],x[1],x[2]))

except:
  print("error")



