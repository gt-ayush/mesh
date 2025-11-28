# Mesh Network Backend (Django)

A simple Django backend that simulates message passing between mesh nodes.
Each node can send and receive messages through REST API endpoints.

---

## Features
- Register mesh nodes
- Store / send messages between them
- Retrieve messages for each node
- Simple REST API built using Django + DRF

---

## Project Structure
backend/
│── manage.py
│── mesh_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── mesh_app/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── routing.py
    └── comm.py

---

## Setup & Run

### 1. Create Virtual Environment
