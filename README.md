# 🚀 AI-Powered Online Code Compiler

An **AI-enhanced online code compiler** that supports **Python, Java, and C** with **error suggestions and user input handling**. Built using **Django, SQLite, and Machine Learning (NLP-based error detection).**  

---

## **🔹 Features**
- 🔦 **Supports Python, Java, and C**  
- 🎯 **AI-Powered Error Detection & Suggestions** (via NLP)  
- ⌨ **Interactive Code Editor with Syntax Highlighting**  
- ⏳ **Execution Time Tracking**  
- 📝 **User Input Support for Code Execution**  
- 📺 **Database Storage for Code History**  
- 🎨 **Modern UI with Bootstrap & CodeMirror**  

---

## **📂 Project Structure**
```
📚 code_compiler/
│── 📂 compiler/                   # Main Django app
│   │── 📂 migrations/              # Database migrations
│   │── 📂 templates/               # HTML templates
│   │   └── home.html               # Main UI template
│   │── 📂 static/                   # Static files (CSS, JS)
│   │── 📝 models.py                 # Database models
│   │── 📝 views.py                  # Django views (code execution logic)
│   │── 📝 urls.py                    # URL routing
│   │── 📝 error_suggestions.py       # AI-based error handling
│── 📝 manage.py                      # Django project manager
│── 📝 requirements.txt               # Dependencies
│── 📝 README.md                      # Project documentation
│── 📝 db.sqlite3                      # SQLite database (auto-generated)
```

---

## **⚙️ Installation**
### **🔹 Prerequisites**
- **Python 3.8+**  
- **Django 4+**  
- **SQLite** (Comes with Django)  
- **pipenv or virtualenv** (Recommended)  

### **🔹 1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/code-compiler.git
cd code-compiler
```

### **🔹 2️⃣ Create a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### **🔹 3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **🔹 4️⃣ Run Migrations**
```bash
python manage.py migrate
```

### **🔹 5️⃣ Start the Django Server**
```bash
python manage.py runserver
```

🔗 **Visit:** `http://127.0.0.1:8000/`

---

## **🖥️ Usage**
### **🔹 Running Code**
1. Select a programming language (**Python, Java, or C**).  
2. Write code in the **CodeMirror Editor**.  
3. (Optional) Provide **user input** in the input box.  
4. Click `▶ Run Code` and see the **output + execution time**.  

### **🔹 Error Handling & AI Suggestions**
If an error occurs, **AI will analyze the error** and suggest fixes.

---

## **🛠️ API Endpoints**
### **1️⃣ Execute Code**
- **URL:** `/execute/`  
- **Method:** `POST`  
- **Request Body (JSON):**
  ```json
  {
    "language": "python",
    "code": "print('Hello World')",
    "user_input": "Vishal"
  }
  ```
- **Response (Success):**
  ```json
  {
    "output": "Hello, Vishal\n",
    "submission_id": 1
  }
  ```
- **Response (Error):**
  ```json
  {
    "error": "SyntaxError: invalid syntax"
  }
  ```

### **2️⃣ Get AI Error Suggestions**
- **URL:** `/error_suggestions/<submission_id>/`  
- **Method:** `GET`  
- **Response:**
  ```json
  {
    "suggestion": "print('Hello, World!')"
  }
  ```

---

## **🌟 To-Do & Future Improvements**
- ✅ **Docker Support**
- ✅ **Deploy to AWS/GCP**
- ✅ **User Authentication (Login, Save Code History)**
- ✅ **More Language Support (JavaScript, C++, etc.)**

---

## **🌟 Contributing**
Want to improve this project?  
1. Fork the repo 🚀  
2. Make changes ✨  
3. Submit a Pull Request 🔥  

---

## **📞 Contact**
💻 Created by **Vishal**  
📧 Email: `vishaal03.it@gmail.com`  


---
