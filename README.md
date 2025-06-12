**IPO WEB APP: **
A production-ready Django + PostgreSQL application for displaying, filtering, and managing IPO listings with a REST API and Bootstrap UI.

---

## Features
~Admin panel for adding/editing companies, IPOs, and documents  
~Public-facing page to display IPO listings with Bootstrap styling  
~Filter by status and search IPOs by company name  
~REST API for IPO, Company, and Document models  
~PostgreSQL integration  
~PDF download links for RHP & DRHP  

---

## Tech Stack

~ **Backend**: Django, Django REST Framework  
~ **Database**: PostgreSQL  
~ **Frontend**: HTML, CSS, Bootstrap 5  
~ **API Testing**: Postman  
~ **Version Control**: Git & GitHub  

---

## Folder Structure
<pre lang="markdown">
ipo_project2/
├── manage.py
├── ipo_project/
├── ipo_app/
├── templates/
│   └── ipo_app/
│       └── ipo_list.html
├── venv/
├── README.md
└── requirements.txt
</pre>
---

## Setup Instructions ##

## 1. Clone the Repository: ##
<pre lang="markdown">
• git clone https://github.com/YOUR_USERNAME/ipo-web-app.git
• cd ipo-web-app
</pre>

## 2. Create Virtual Environment: ##
<pre lang="markdown">
python3 -m venv venv
source venv/bin/activate
</pre>

## 3. Install Requirements: ##
<pre lang="markdown">
pip install -r requirements.txt
</pre>

## 4. Set Up PostgreSQL Database: ##
<pre lang="markdown">
CREATE DATABASE ipo_db;
CREATE USER ipo_user WITH PASSWORD 'password123';
GRANT ALL PRIVILEGES ON DATABASE ipo_db TO ipo_user;
</pre>

## 5. Update settings.py with: ##
<pre lang="markdown">
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ipo_db',
        'USER': 'ipo_user',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
</pre>


## 6. Run Migrations

<pre lang="markdown">
python manage.py makemigrations
python manage.py migrate
</pre>


## 7. Create Admin User
<pre lang="markdown">
python manage.py createsuperuser
</pre>

## 8. Run the Server
<pre lang="markdown">
python manage.py runserver
</pre>

## **Access the App**
	•	Public IPO Listings: http://127.0.0.1:8000/
	•	Admin Panel: http://127.0.0.1:8000/admin/
	•	API Endpoints:
	•	/ipo/api/companies/
	•	/ipo/api/ipos/
	•	/ipo/api/documents/

## **Developer Notes**
	•	Add IPOs through the Django admin panel after login
	•	RHP/DRHP files are assumed to be external PDF URLs for now
	•	You can expand the app with user auth, API tokens, or dashboard stats

⸻

__Credits__
<pre lang="markdown">
Developed as part of Bluestock Fintech internship.
Maintained by Konark.
</pre>
