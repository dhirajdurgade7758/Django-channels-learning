# Django Channels Counting App

This project is a simple Django application demonstrating real-time WebSocket communication using Django Channels. It features a basic counting app and a chat interface, showcasing both synchronous and asynchronous consumers for handling WebSocket connections.

---

## 🚀 Features

- 🔄 Real-time counter updates via WebSocket
- 🔁 Example of both synchronous and asynchronous consumers
- 💬 Simple chat input and log area (front-end)
- ⚙️ Django 4.2 with Channels 4 and Daphne ASGI server
- 🧪 Minimal setup for learning and experimentation

---

## 📁 Project Structure
```
gs1/
├── db.sqlite3
├── manage.py
├── app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── consumers.py
│   ├── models.py
│   ├── routing.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── gs1/
│           └── index.html
├── gs1/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd django-channels
   ```
2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations and start the server:**
   ```bash
   cd gs1
   python manage.py migrate
   python manage.py runserver
   ```
5. **Open in browser:**
   
   Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ⚙️ How It Works

- The main page (`index.html`) connects to a WebSocket endpoint
- `MySyncConsumer` and `MyAsyncConsumer` handle real-time WebSocket communication
- The counter is updated every second and streamed to the client
- The chat input is a placeholder for future enhancements

---

## 🧩 Key Files

- `app/consumers.py`: Contains both synchronous and asynchronous WebSocket consumers
- `app/routing.py`: Defines WebSocket URL routing
- `gs1/asgi.py`: ASGI application setup for Channels
- `app/templates/gs1/index.html`: Front-end template with JavaScript WebSocket logic

---

## 📦 Requirements

See `requirements.txt`:
```txt
channels==4.0.0
daphne==4.0.0
asgiref==3.6.0
django==4.2
```

---

## 🔧 Extending

- Add models and views for advanced real-time features
- Expand the chat interface to include user messages
- Integrate Django authentication for group-based messaging and private rooms

---

## 📄 License

This project is for educational purposes only.
