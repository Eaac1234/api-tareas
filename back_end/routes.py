import taskService
from fastapi import APIRouter
from pydantic import BaseModel

class tasks(BaseModel):
    Title : str
    Descripcion :str



router=APIRouter()

#dentro de la url,solo datos que identifiquen cosas

@router.get("/tasks")
def get_task():
    return taskService.show()

@router.post("/task")
def created_task(task:tasks):
    return taskService.insert(task.Title,task.Descripcion)


@router.put("/task/{id}")
def update_task(id:int,task:tasks):
    return taskService.update(id,task.model_dump())

@router.delete('/task/{id}')
def delete_task(id:int):
    return taskService.delete(id)