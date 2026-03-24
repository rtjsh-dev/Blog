# 📰 Django Blog — Full-Stack Blogging Platform

> A production-ready blogging system built with Django, featuring multi-role access control, rich content management, and a fully deployed live environment on PythonAnywhere.

---

## 🖼️ Preview

![Django Blog Homepage](screenshot.png)

A news-style blog platform with category navigation, featured posts, hero banners, search, and role-based dashboards — all built from scratch in Django.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🔐 Multi-role system | Admin / Manager / Editor / Author with scoped permissions |
| 📝 Full CRUD | Create, Read, Update, Delete for posts & categories |
| 🔗 Slug generation | Unique slugs auto-generated and prepopulated |
| 🖼️ Media uploads | Image upload & configuration per post |
| 💬 Comment system | Authenticated users only |
| 📊 Dashboards | Manager & Editor dashboards with counts and tables |
| 🔍 Search | Search with retained query in the input field |
| 📄 Pagination | Clean pagination across listing pages |
| ⭐ Featured posts | Highlighted posts on the homepage |
| 🌐 Deployed | Live on PythonAnywhere |

---

## 🧠 What You'll Learn

- **Project structure** — Real-world Django folder layout and app organisation
- **Models** — Blog, Category, Comment, User relations, slugs, media handling
- **Forms** — Create/edit posts, user registration, comment submission
- **Authentication & Authorisation** — Login, logout, Groups, Permissions, decorators
- **Admin customisations** — Custom listings and display in the Django admin panel
- **Dashboards** — Role-based views for Editors and Managers with permission checks
- **Search & Pagination** — Search with retained input, paginated results
- **File & Static handling** — Media uploads, static files configuration, templates
- **Deployment** — Full checklist and step-by-step guide for PythonAnywhere

> This project focuses on **practical features used in production blogging systems** and how to structure code for clarity and maintainability.

---

## 🛠️ Tech Stack

- **Backend** — Python 3.10+, Django 5.x
- **Frontend** — HTML, CSS, Bootstrap 4, crispy-forms
- **Database** — SQLite (development) / PostgreSQL or MySQL (production)
- **Deployment** — PythonAnywhere
- **Auth** — Django's built-in auth system with Groups & Permissions

---

## 📋 Requirements

- Python **3.10+** (3.12 recommended)
- Django **5.x** — always use the latest stable version (see `requirements.txt`)
- A virtual environment tool (`venv` or `virtualenv`)
- SQLite for development, PostgreSQL / MySQL for production
- *(Optional)* nginx / gunicorn for advanced deployments — contact me for a guide

---

## ⚙️ Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/django-blog.git
cd django-blog

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser
python manage.py createsuperuser

# 6. Collect static files
python manage.py collectstatic

# 7. Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 🗂️ Project Structure

```
Blog/
├── Blog/               # Project settings & URLs
├── Blog_app/           # Main application (models, views, forms)
│   ├── models.py       # Post, Category, Comment models
│   ├── views.py        # All views including dashboards
│   ├── forms.py        # Post, comment, registration forms
│   └── admin.py        # Custom admin configuration
├── dashboard/          # Manager & Editor dashboard views
├── template/           # HTML templates
├── static/             # CSS, JS, images
├── media/              # User-uploaded files
├── migrations/         # Database migrations
├── manage.py
└── requirements.txt
```

---

## 👥 User Roles

| Role | Permissions |
|---|---|
| **Admin** | Full access including Django admin panel |
| **Manager** | Dashboard access, manage all posts & categories |
| **Editor** | Dashboard access, manage assigned posts |
| **Author** | Create and manage own posts |
| **Visitor** | Read posts, use search; must log in to comment |

---

## 🌍 Deployment (PythonAnywhere)

1. Upload or clone your repo to PythonAnywhere
2. Create a virtual environment with Python 3.12
3. Install dependencies: `pip install -r requirements.txt`
4. Set `STATIC_ROOT` and `STATICFILES_DIRS` in `settings.py`
5. Run `python manage.py collectstatic`
6. Configure the **Static Files** mapping in the PythonAnywhere Web tab:
   - URL: `/static/` → Directory: `/home/<username>/Blog/staticfiles/`
7. Set up your WSGI file and reload the web app

---

## 📬 Contact

For advanced deployment setups (nginx + gunicorn), custom features, or questions — feel free to reach out!

---

## 📄 License

This project is for educational purposes. Feel free to fork and build upon it.
