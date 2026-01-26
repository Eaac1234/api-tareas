from database import get_connection,disconnect
from random import randint
from datetime import datetime
from models import task


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
    task.ID=id
    task.Title=title
    task.Descripcion=descripcion
    task.State=0
    task.Created=date
    task.Last_Update=update
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
            "ID":task.ID,
            "Title":task.Title,
            "Descripcion":task.Descripcion,
            "State":task.State,
            "Created":task.Created,
            "Last_update":task.Last_Update
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
    task.ID=id
    if checkout(cursor):
        return {
            "Status":"successful",
            "msg":"Tarea Editada",
            "Task":{
                "ID":task.ID
            }
        }
    else:
        return {
            "Status":"Failed",
            "msg":"No se pudo encontrar la tarea a editar",
            "Task":{
                "ID":task.ID
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
    task.ID=id
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
                "ID":task.ID
            }
        }
    
    else:
        disconnect(connect)
        return {
            "Status":"Failed",
            "msg":"Tarea no encontrada",
            "Task":{
                "ID":task.ID
            }
        }
    


def show():
    tasks=[]
    cursor,connect=get_connection()
    cursor.execute(
        """
        SELECT *FROM tasks
        """
    )
    registers=cursor.fetchall()
    for a in registers:
        print(a)
    
    tasks=show_task(connect,registers,len(registers)-1,tasks)
    return{
        "Status":"successful",
        "msg":"Tareas disponibles",
        "tasks":tasks
    }


def show_task(connect,registers,i:int,info:list):
    if i<0:
        disconnect(connect)
        return info
    else:
        tasks=task(ID=registers[i][0], Title=registers[i][1],Descripcion=registers[i][2],State=registers[i][3],Created=registers[i][4],Last_Update=registers[i][5])
        i-=1
        info.append(tasks)
        return show_task(connect,registers,i,info)
    



#dictionary={"Title":"Alberto","Descripcion":"Arcos"}
show()
#print(update(578772197,dictionary))
#show()



