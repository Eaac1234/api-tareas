from database import get_connection,disconnect
from random import randint
from datetime import datetime

def created_id():
    id=''
    for i in range(10):
        id=id+str(randint(1,9))
    return int(id)

def get_date():
    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return date
    
def checkout():
    pass

def insert(title:str,descripcion:str):
    id=created_id()
    date=get_date()
    state=1
    update="None"
    cursor,connect=get_connection()
    cursor.execute(
        """
        INSERT INTO tasks
                    (ID,Title,Descripcion,State,Created,Last_Update) VALUES(?,?,?,?,?,?)
        """,(id,title,descripcion,state,date,update)
    )
    connect.commit()
    disconnect(connect)

def update(id:int,i:list):
    update=["Title","Descripcion","State"]
    date=date
    cursor,connect=get_connection()
    cursor.execute("""
    UPDATE tasks SET 
    """)
    disconnect(connect)

def delete(id:int):
    cursor,connect=get_connection()
    id=int(id)
    cursor.execute(
        """
        DELETE FROM tasks WHERE ID==?
        """,(id,)
    )
    if cursor.rowcount==1:
        connect.commit()
        disconnect(connect)
        return True
    else:
        disconnect(connect)
        return False

def show():
    cursor,connect=get_connection()
    cursor.execute(
        """
        SELECT *FROM tasks
        """
    )
    registers=cursor.fetchall()
    for a in registers:
        print(a)
    disconnect(connect)

insert('hola','hola')
show()
#print("\n")
#print(delete(5361872372))
#show()
