import sqlite3

class Table():
    def __init__(self):
            self.connection = sqlite3.connect("db/todo_list.db",check_same_thread=False, isolation_level=None)
            self.cursor = self.connection.cursor()

    def read_data(self):
        query = "SELECT * FROM to_do_app"
        result= self.connection.execute(query)    
        tasks = result.fetchall()
        return tasks

    def add_new_task(self,title,description,status,time):
                query = f"INSERT INTO to_do_app(titel,description,status,time) VALUES ('{title}','{description}','{status}','{time}')"
                self.cursor.execute(query)
                self.connection.commit()
                return True  
 
    def delet_tasks(self,id):
        self.cursor.execute(f"SELECT * from to_do_app WHERE id = '{id}' ")
        task = self.cursor.fetchall()
        if len(task) == 0 :
              return False
        else :
            query = f"DELETE FROM to_do_app WHERE id = {id}"
            self.cursor.execute(query)
            self.connection.commit()
            return True  
    
    def task_done(self,id):
        self.cursor.execute(f"SELECT * FROM  to_do_app WHERE id ='{id}'")
        task = self.cursor.fetchone()
        if len(task) <1:
              return False
        else :
            self.cursor.execute(f"UPDATE to_do_app SET status ='1' WHERE id ='{id}'")
            self.connection.commit()
            return True
        
   
