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


# **1 — Go to Backend Folder**

```bash
cd ~/Desktop/mesh/backend
```

---

#  **2 — Create & Activate Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

You should now see:

```
(venv) ayush@...
```

---

#  **3 — Install Requirements**

Your root folder already contains `requirements.txt`.

Run this:

```bash
pip install -r ../requirements.txt
```

This installs:

* Django
* Channels
* Any other dependencies you added
  (If requirements.txt is empty → tell me, I’ll generate one.)

---

# **4 — Apply Migrations**

```bash
python3 manage.py migrate
```

📌 *No output = NORMAL (Django shows nothing when everything is OK).*

---

#  **5 — Run Server**

```bash
python3 manage.py runserver
```

Expected output:

```
Watching for file changes with StatReloader
Django version 5.x
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

If you do **NOT** see that → tell me the last line you see.

---

# 🔥 **6 — Test the API (New Terminal Window)**

Open a **second terminal**:

```bash
cd ~/Desktop/mesh/backend
source venv/bin/activate
```

### Send a message:

```bash
curl "http://127.0.0.1:8000/send/?msg=Hello"
```

Expected JSON:

```json
{"status": "stored", "message": "Hello"}
```

### Receive messages:

```bash
curl "http://127.0.0.1:8000/receive/"
```

Expected output:

```json
{"messages": ["Hello"]}
```

---

# ⚠️ **If curl says “Couldn’t connect to server”**

One of these is wrong:

### 1 The server is *not running*

Make sure the FIRST terminal still shows:

```
Starting development server at http://127.0.0.1:8000/
```

### 2 Your URL routes are incorrect

Open:
`backend/mesh_project/urls.py`

Must contain:

```python
from django.urls import path, include

urlpatterns = [
    path('', include('mesh_app.urls')),
]
```

Open:
`backend/mesh_app/urls.py`

Must contain:

```python
from django.urls import path
from .views import send_message, receive_messages

urlpatterns = [
    path('send/', send_message),
    path('receive/', receive_messages),
]
```

### 3 Another app is using port 8000

Try:

```bash
python3 manage.py runserver 8080
```

Then test:

```bash
curl "http://127.0.0.1:8080/send/?msg=Hello"
curl "http://127.0.0.1:8080/receive/"
```

---

# 🎉 You're 100% ready

Your structure, files, and project layout are **correct**.

If the server STILL shows no output when running `runserver`, tell me exactly what the terminal prints — I’ll fix it instantly.

Just copy & paste the last lines you see.


