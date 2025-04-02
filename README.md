# 📘 UniBook - University Resource Management

UniBook is a **web-based platform** designed to help university students manage their academic resources, collaborate with peers, and stay organized.

## 🚀 Features
- 📚 **Notes Sharing**: Upload, view, and download study materials.
- ✅ **Assignment Tracker**: Keep track of deadlines and pending tasks.
- 💬 **Discussion Forum**: Connect with peers and ask academic questions.
- 🔍 **Search & Filter**: Easily find notes and discussions.
- 🔒 **User Authentication**: Secure login and signup functionality.

---
## 📌 Github Repository
Find the source code here: [https://github.com/vaibhav-singh05/UniBook](https://github.com/vaibhav-singh05/UniBook)

---
## 🛠 Installation & Setup
Follow these steps to set up the project:

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/vaibhav-singh05/UniBook.git
cd UniBook
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
```
- **Activate it:**
  - **Windows:** `venv\Scripts\activate`
  - **Mac/Linux:** `source venv/bin/activate`

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Apply Database Migrations**
```sh
python manage.py migrate
```

### **5️⃣ Run the Development Server**
```sh
python manage.py runserver
```
- Now, open **http://127.0.0.1:8000/** in your browser.

---
## 🔑 Authentication
UniBook includes **secure user authentication** for safe access to resources.

### **1️⃣ Register/Login**
- Users must sign up or log in to access full features.

---
## 🏗 Project Structure
```
UniBook/
├── Hello/                  # Root Django project directory
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # Entry point
│
├── templates/               # Frontend templates
│   ├── index.html
│   ├── about.html
│   ├── cart.html
│   ├── checkout.html
│   ├── login.html
│   ├── my_profile.html
│   ├── product_detail.html
│   ├── register.html
│   ├── sell.html
│   ├── update_profile.html
│
├── static/                  # Static assets
│   ├── img/
│   │   ├── about1.jpg
│   │   ├── about2.jpg
│   │   ├── about3.jpg
│   │   ├── usericon.png
│
├── home/                    # Main application
│   ├── models.py            # Database models
│   ├── views.py             # Views/Controllers
│   ├── urls.py              # App-specific routing
│   ├── admin.py             # Admin panel config
│
├── db.sqlite3               # Database file
├── manage.py                # CLI Management script
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---
## ✨ Contributing
1. Fork the repo 🍴
2. Create a new branch 🌿
3. Commit your changes 🎯
4. Push to GitHub 🚀
5. Submit a **Pull Request** 💡

---
## 📞 Support
- **Author:** Vaibhav Singh  
- **Email:** vaibhavsingh273010@gmail.com  
- **LinkedIn:** [Click Here](https://www.linkedin.com/in/vaibhav-singh-2a5991229/)  

---
### 🎉 **Happy Coding! 🚀**

