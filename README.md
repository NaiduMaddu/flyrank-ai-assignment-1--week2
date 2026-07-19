# 📝 FastAPI Todo CRUD API

A simple Todo CRUD API built using **FastAPI** and **Pydantic**. This project demonstrates basic REST API development with in-memory data storage.

## 🚀 Features

- Create a new todo
- Read a todo by ID
- Update an existing todo
- Delete a todo
- Automatic API documentation with Swagger UI
- Input validation using Pydantic

---

## 🛠️ Tech Stack

- FastAPI
- Pydantic
- Uvicorn
- Python 3.x

---

## 📂 Project Structure

```
.
├── main.py
├── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install fastapi uvicorn
```

---

## ▶️ Running the API

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📌 API Endpoints

### Home

| Method | Endpoint |
|--------|----------|
| GET | `/` |

---

### Create Todo

| Method | Endpoint |
|--------|----------|
| POST | `/tasks` |

Example Request

```json
{
    "title": "Learn FastAPI",
    "completed": false
}
```

---

### Get Todo

| Method | Endpoint |
|--------|----------|
| GET | `/tasks/{id}` |

---

### Update Todo

| Method | Endpoint |
|--------|----------|
| PUT | `/tasks/{id}` |

Example Request

```json
{
    "title": "Learn LangGraph",
    "completed": true
}
```

---

### Delete Todo

| Method | Endpoint |
|--------|----------|
| DELETE | `/tasks/{id}` |

---

## 🧪 Testing

Use Swagger UI to test every endpoint without writing any frontend code.

```
http://127.0.0.1:8000/docs
```

---

## 📚 Learning Objectives

This project helped me understand:

- Building REST APIs using FastAPI
- CRUD Operations
- Path Parameters
- Request Body Validation using Pydantic
- Working with Python dictionaries and lists
- Automatic API documentation with Swagger UI

---

## 🚧 Future Improvements

- SQLite Database Integration
- SQLAlchemy ORM
- Proper HTTP Status Codes
- HTTPException for error handling
- Response Models
- Authentication using JWT
- Docker Support

---

## 📄 License

This project is created for learning purposes.
