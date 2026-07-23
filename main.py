from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from sqlalchemy import Column,Integer,String,Boolean
from dotenv import load_dotenv
load_dotenv()
engine=create_engine(os.getenv("DATABASE_URL"))
Base=declarative_base()
class Todo(Base):
     __tablename__="tasks"
     id=Column(Integer,primary_key=True,index=True)
     title=Column(String,nullable=True)
     completed=Column(Boolean,nullable=True)
Base.metadata.create_all(bind=engine)
session_local=sessionmaker(bind=engine)
db=session_local()
app=FastAPI()
class Model(BaseModel):
    id:int
    title:str
    completed:bool
@app.get("/")
def start():
    return "Hello world"
@app.post("/tasks")
def create(task:Model):
    task=Todo(title=task.title,completed=task.completed)
    db.add(task)
    db.commit()
    return f"Successfully added to to-do task {task.title}"
@app.get("/tasks/{id}")
def read_todo(id:int):
        tasks = db.query(Todo).all()
        if len(tasks)>0:
            for todo in tasks:
                if todo.id==id:
                    return {
                         "id":todo.id,
                         "title":todo.title,
                         "completed":todo.completed
                    }
        else:
            return "Oops i could't find your todo"
@app.put("/tasks/{id}")
def update(task:Model):
    todo = db.query(Todo).filter(Todo.id ==task.id).first()
    if todo is None:
         return "Oops we couldn't find the todo"
    else:
        todo.title=task.title
        todo.completed=task.completed
        db.commit()
        return f"Successfully updated your to-do here is the updated one"
@app.delete("/tasks/{id}")
def delete(id:int):
    todo=db.query(Todo).filter(Todo.id==id).first()
    if todo is None:
         return "Oops we couldn't find the todo"
    else:
        db.delete(todo)
        db.commit()
        return "Successfully deleted the todo"


