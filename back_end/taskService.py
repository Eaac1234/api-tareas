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
    
def checkout(cursor):
    if cursor.rowcount !=0:
        return True
    else :
        return False



def insert(title:str,descripcion:str):
    id=created_id()
    date=get_date()
    state=0
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
    return {
        "status":"Succesful",
        "msg":"created user",
        "info":{
            "ID":id,
            "Title":title,
            "Descripcion":descripcion,
            "State":state,
            "Created":date,
            "Last_update":update
        }
    }



def update(id:int,i:dict):
    copy_values=[]
    copy_keys=[]
    date=get_date()
    i["State"]=1
    i["Last_Update"]=date
    for key,value in i.items():
        copy_keys.append(key)
        copy_values.append(value)
  
    
    cursor,connect=get_connection()
    update_commit(id,cursor,connect,copy_keys,copy_values,len(copy_keys)-1)
    disconnect(connect)
    if checkout(cursor):
        return {
            "Status":"successful",
            "msg":"Tarea Editada",
            "Task":{
                "ID":id
            }
        }
    else:
        return {
            "Status":"Failed",
            "msg":"No se pudo encontrar la tarea a editar",
            "Task":{
                "ID":id
            }
        }

  

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
    if checkout(cursor):
        connect.commit()
        disconnect(connect)
        return {
            "Status":"successful",
            "msg":"Tarea eliminada",
            "Task":{
                "ID":id
            }
        }
    
    else:
        disconnect(connect)
        return {
            "Status":"Failed",
            "msg":"Tarea no encontrada",
            "Task":{
                "ID":id
            }
        }
    


def show():
    cursor,connect=get_connection()
    cursor.execute(
        """
        SELECT *FROM tasks
        """
    )
    registers=cursor.fetchall()
    return show_task(connect,registers)

def show_task(connect,registers):
    print("Tus tareas pendientes")
    for a in registers:
        print(a)
    disconnect(connect)



#dictionary={"Title":"Alberto","Descripcion":"Arcos"}
#show()
#print(update(578772197,dictionary))
#show()


