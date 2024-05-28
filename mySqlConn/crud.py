import pymysql

class Database:

    def __init__(self):
       self.con = pymysql.connect(user='root', host='localhost', password='MRAK#7899@yk', db='pythonconnect')

       q = "CREATE TABLE IF NOT EXISTS user(userId int primary key, user_name varchar(100), phone varchar(12))"

       cur = self.con.cursor()
       cur.execute(q)
    #    print("Table Created Successfully!")

    #Inserting data into the table

    def insert_data(self, userId, user_name, phone):
        q = """insert into user(userId, user_name, phone) 
            values({},'{}','{}') """.format(userId, user_name, phone)
      
        cur  = self.con.cursor()
        cur.execute(q)
        self.con.commit()
        print("Inserted successfully!")
    
    #fetch data
    def get_data(self):
        cur = self.con.cursor()
        q = "select * from user"
        cur.execute(q)
        res = cur.fetchall()
        for x in res:
            print(x)
        


db = Database()
# db.insert_data(2, 'Ankit', '7078427126')
db.get_data()