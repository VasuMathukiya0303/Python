import sqlite3
class myconnect:
      
      def __init__(self):
            self.conn = sqlite3.connect("emp.db")    
            try:
                  self.conn.execute('create table if not exists Employee(name text, salary integer, emp_type char')
            except:
                  pass
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            conn=sqlite3.connect('emp.db')
            conn.execute('insert into Employee values(NULL,?,?,?,?,?,?)',(ename,eemail,emob,etype,eexp,esalary))
            conn.commit()
            conn.close()

      def display(self):
             id=int(input("Enter the emp id:"))
             conn=sqlite3.connect('emp.db')
             data=conn.execute('select * from Employee where id = ?',(id,))
             v=0
             for row in data:
                 v=1
                 print("******************************************************")
                 print("name:",row[1])
                 print("email:",row[2])
                 print("mobile_no:",row[3])
                 print("employee type:",row[4])
                 print("experience:",row[5])
                 print("salary:",row[6])
                 print("*******************************************************")
             if(v==0):
                print("Please, Enter valid ID")
             conn.close()
      
