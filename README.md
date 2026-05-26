# 🏥 Evercare - Elder Care Management System

**Evercare** is a comprehensive health and service management platform designed specifically to provide seamless care and support for the elderly. The system bridges the gap between elderly citizens, their families, and healthcare professionals (Doctors and Caretakers), ensuring health monitoring, emergency assistance, and professional care are just a few clicks away.

---

## 🌟 Key Features

### 👴 Elderly Profile Management
*   **Multiple Profiles:** Users can create and manage detailed profiles for multiple elderly family members.
*   **Medical History:** Maintain a history of medical conditions and emergency contact details.

### 🩺 Health Monitoring & Analytics
*   **Vital Tracking:** Track essential health metrics including Blood Pressure, Sugar Levels, Heart Rate, Weight, and Temperature.
*   **Trend Analysis:** View health records over time to monitor recovery or detect potential health issues.

### 💊 Medicine Management
*   **Dosage Scheduling:** Set up medication names, dosages, and frequencies.
*   **Tracking:** Keep track of start and end dates for various medication cycles.

### 📅 Service Booking & Management
*   **Professional Care:** Book verified Doctors and Caretakers for home visits.
*   **Admin Approval Workflow:** Secure booking process with administrative oversight and confirmation.
*   **Real-time Status:** Track the status of bookings from "Pending" to "Completed".

### 🆘 SOS Emergency Alert System
*   **Instant Alerts:** Trigger emergency SOS alerts with a single click.
*   **Admin Notification:** Immediate routing of alerts to the administrative dashboard for rapid response.

### 💳 Payment Integration
*   **Seamless Checkout:** A streamlined payment workflow for service bookings.
*   **Transaction Tracking:** Automated generation of transaction records and payment history.

### 💬 Real-Time Communication
*   **Chat System:** Integrated communication platform for interacting with healthcare professionals (via WebSocket/ASGI).

---

## 🛠️ Technology Stack

*   **Backend:** [Django](https://www.djangoproject.com/) (Python Framework)
*   **Database:** SQLite (Development)
*   **Real-time Features:** Daphne (ASGI Server)
*   **Frontend:** HTML5, CSS3, JavaScript
*   **Media Management:** Pillow (for Image Processing)

---

## 📂 Project Structure

```text
evercare/
├── app_modules/
│   ├── adminapp/       # Administrative controls and service management
│   └── userapp/        # User dashboard, profile, and health modules
├── evercare/           # Project configuration (settings, urls, asgi/wsgi)
├── media/              # User-uploaded images (profiles, doctor images)
├── static/             # CSS, JS, and image assets
├── templates/          # HTML templates for User and Admin dashboards
├── manage.py           # Django management script
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
*   Python 3.8 or higher
*   pip (Python package manager)

### 2. Installation
Clone the repository and navigate to the project directory:
```bash
git clone <repository-url>
cd evercare
```

### 3. Setup Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install django daphne pillow
```

### 5. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 7. Run the Application
```bash
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`

---

## 👥 Roles & Permissions

*   **Admin:** Manages services (Doctors/Caretakers), approves bookings, resolves emergency alerts, and views reports.
*   **User:** Manages elderly profiles, tracks health records, books services, and triggers SOS alerts.
*   **Doctor/Caretaker:** Healthcare professionals who provide services to the elderly users.

---

## 📄 License

This project is developed for **Evercare** healthcare solutions. All rights reserved.

---

> [!TIP]
> For any technical support or contributions, please contact the development team or open an issue in the repository.
