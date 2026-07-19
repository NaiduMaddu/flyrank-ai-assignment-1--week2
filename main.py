from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
todo_list=[]
class Model(BaseModel):
    title:str
    completed:bool
@app.get("/")
def start():
    return "Hello world"
@app.post("/tasks")
def create(task:Model):
    todo_list.append({"id":len(todo_list)+1,
        "title":task.title,
        "completed":task.completed})
    return f"Successfully added to to-do task {task.title}"
@app.get("/tasks/{id}")
def read_todo(id:int):
        if len(todo_list)>0:
            for todo in todo_list:
                if todo["id"]==id:
                    return todo
        else:
            return "Oops i could't find your todo"
@app.put("/tasks/{id}")
def update(id:int,task:Model):
    for todo in todo_list:
        if todo["id"]==id:
            todo["title"]=task.title
            todo["completed"]=task.completed
            return f"Successfully updated your to-do here is the updated one {todo_list[id-1]}"
    else:
        return "Oops your todo is found please try again"
@app.delete("/tasks/{id}")
def delete(id:int):
    for todo in todo_list:
        if todo["id"]==id:
            todo_list.remove(todo)
            return "Your todo is Successfully deleted"
    else:
            return "Oops your to-do not found please try again"




