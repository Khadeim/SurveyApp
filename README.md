# SurveyApp

A Django-based survey system that allows users to register, log in, and participate in surveys.
The project includes an administrative panel for managing users and system data by Khadeim Rahman.

---

# Requirements

* Python **3.11**
* pip

⚠️ This project was originally developed with an older Python version and repurposed and worked on as a challenge to test my knowledge and understanding. Running it with **Python 3.13+ may cause compatibility issues**, so Python **3.11 is recommended**.

---

# Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/SurveyApp.git
cd SurveyApp
```

### 2. Create a virtual environment

Windows:

```bash
python3.11 -m venv venv
```

Mac/Linux:

```bash
python3.11 -m venv venv
```

---

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

You should now see `(venv)` in your terminal.

---

### 4. Install project dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the Django server

```bash
python manage.py runserver
```

Then open the application in your browser:

```
http://127.0.0.1:8000/
```

---

# Admin Access

An admin account has been preconfigured in the system.

**Username**

```
admin@shangrila.gov.un
```

**Password**

```
shangrila@2021$
```

The admin panel can be accessed at:

```
http://127.0.0.1:8000/admin/
```

---

# Demonstration User

A demonstration user has been created to showcase system functionality.

**Username**

```
kr238
```

This user uses the following **SNI**:

```
CB8FBCCM
```

When registering a new user, please keep this SNI in mind as duplicate SNIs are not be allowed.

---

# User Management

Users can also be created or managed directly through the **Django Admin Panel** for convenience.

By logging in as an admin and navigating to:

```
http://127.0.0.1:8000/admin/
```

the demonstration user (`kr238`) can be removed if needed along with other users for testing purposes.

---

# Notes

* The project uses **SQLite** as its default database.
* A virtual environment is recommended to isolate dependencies.
* Ensure the virtual environment is activated before running the project.

To deactivate the virtual environment:

```bash
deactivate
```
