#source code for vaccine management

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Vaccine_Management",
  autocommit=True
)
if mydb.is_connected()==True:
	print("Successfully connected to Database")
mycursor = mydb.cursor()
#database creation
mycursor.execute("CREATE DATABASE IF NOT EXISTS Vaccine_Management")
#table creation
mycursor.execute("CREATE TABLE IF NOT EXISTS Vaccine (Vaccine_name  VARCHAR(255) NOT NULL, MANUFACTURER VARCHAR(255) NOT NULL , STOCKS INT) ") 



 

#code for new vaccine addup
def add():
		print("Enter the details of vaccine add()")
		v_name=input("Enter vaccine name:")
		m=input("Enter name of manufacturer:")
		stk=int(input("Enter the no. of stocks:"))
		val=(v_name,m,stk)
		sql="INSERT INTO Vaccine(Vaccine_name,MANUFACTURER,STOCKS) VALUES (%s,%s,%s)"
		mycursor.execute(sql, val)
		print(mycursor.rowcount,"record added.")
		
#code for updating of details		
def update():
	vaxnm=input("vaccine that you want to update update(): ")
	newvaxnm=input("Enter the updated name of vaccine: ")
	newmanfnm=input("Enter updated name of manufacturer: ")
	mycursor.execute("UPDATE Vaccine SET Vaccine_name='%s', MANUFACTURER='%s' WHERE Vaccine_name='%s'"%(newvaxnm,newmanfnm,vaxnm))
	
#code for updating vaccine stocks	
def updatestk():
	vnme=input("vaccine that you want to update stock of updatestk(): ")
	stok=input("number of stock you want to update: ")
	mycursor.execute("UPDATE Vaccine SET STOCKS='%s'  WHERE Vaccine_name='%s'"%(stok,vnme))
#code for vaccine record showup
def showrecord():
	mycursor.execute("select * from Vaccine")
	data=mycursor.fetchall()
	if data ==None:
		print("Empty set")
	else:
		for row in data:
			print(row)
		count=mycursor.rowcount
		print("rows retrieved", count)
#code for deleting vaccine
def delete():
	vname=input("Enter the vaccine name you want to remove:")
	mql="DELETE FROM Vaccine WHERE Vaccine_name='%s'"%(vname)
	mycursor.execute(mql)
	print("record removed.")
		
while True:
	print("Welcome to Vaccination Services")
	print("Type: 1 for adding new vaccine details \n 2 for updating vaccine details\n 3 for updating vaccine stocks \n 4 for showing all data \n 5 for deleting vaccine  \n 6 for exit "  )
	x=int(input("Enter the desired number: "))
	if x==1:
		add()
	if x==2:
		update()
	if x==3:
	    updatestk()
	if x==4:
	    showrecord()
	if x==5:
	   delete()
	if x==6:
	   mycursor.close()
	   mydb.close()
	   if mydb.is_connected()==False:
	   	print("Successfully disconnected to Database")
	   	print("Thank you")
	   	break