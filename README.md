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
```
ayush@ayush-83eq:~/Desktop/mesh$ tree
.
├── backend
│   ├── manage.py
│   ├── mesh_app
│   │   ├── comm.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routing.py
│   │   ├── urls.py
│   │   └── views.py
│   └── mesh_project
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
├── docs
│   ├── architecture.md
│   ├── demo-plan.md
│   └── overview.md
├── frontend
│   ├── static
│   │   ├── app.js
│   │   └── styles.css
│   └── templates
│       └── index.html
├── LICENSE
├── package.json
├── README.md
├── requirements.txt
└── tests
    ├── test_comm.py
    └── test_node.py

9 directories, 23 files

```
---

## Setup & Run

### 1. Create Virtual Environment
