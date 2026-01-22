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
    copy_values=[]
    copy_keys=[]
    date=get_date()
    date={"Last_Update":date}
    i.append(date)
    for d in i:
       copy_keys.append(list(d.items())[0][0])
       copy_values.append(list(d.items())[0][1])
    cursor,connect=get_connection()
    update_commit(id,cursor,connect,copy_keys,copy_values,len(copy_keys)-1)
    disconnect(connect)

def update_commit(id:int,cursor,connect,keys:list,values:list,i:int):
    if i<0:
        connect.commit()
        return True
    else:
        key=keys[i]
        value=values[i]
        sql = f"""
        UPDATE tasks
        SET {key} = ?
        WHERE ID = ?
        """
        cursor.execute(sql,(value,id))
        i -=1
        update_commit(id,cursor,connect,keys,values,i)
     


     




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

#insert('hola','hola')
#show()
#print("\n")
#print(delete(5361872372))
#show()

#lista=[{"Title":"hola mate"},{"Descripcion":"hola como estas eduardo"},{"State":0}]
#delete(2327134934)
#update(6175357414,lista)
#show()