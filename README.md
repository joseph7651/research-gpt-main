# Django Project Setup Guide

Welcome!  
Follow these instructions to set up and run the project on your local machine.

---

## Requirements

- Python 3.9 or higher (recommended: 3.10)
- pip (Python package installer)
- virtualenv (recommended)
- PostgreSQL or SQLite (depending on project settings)

---

## 1. Extract the ZIP File

- **Windows**: Right-click the `.zip` → "Extract All" → choose a location.
- **Mac**: Double-click the `.zip` → it will extract into a folder.

---

## 2. Open Terminal or Command Prompt

- **Windows**: Press `Win + R`, type `cmd`, and press Enter.
- **Mac**: Open `Terminal` from `Applications > Utilities > Terminal`.

---

## 3. Navigate to the Project Directory

```bash
cd path/to/your/project

---

🛠️ 4. Create and Activate a Virtual Environment
Windows
 - python -m venv env
 - env\Scripts\activate
Mac/Linux
 - python3 -m venv env
 - source env/bin/activate

⚡ Tip: If venv is not available, install it using:
    pip install virtualenv

📦 5. Install Project Dependencies
    - pip install -r requirements.txt

🗄️ 6. Apply Database Migrations
    - python manage.py migrate

   7. Running in Development Mode
        - To start Django Tailwind in development mode, run the following command in a terminal:

        - python manage.py tailwind start


🚀 8. Run the Development Server
    - python manage.py runserver
# touched on 2025-08-14T20:06:58.342808Z
# touched on 2025-08-14T20:07:05.354617Z
# touched on 2025-08-14T20:07:11.968996Z
# touched on 2025-08-14T20:07:19.247176Z
# touched on 2025-08-14T20:07:35.230070Z
# touched on 2025-08-14T20:07:41.967994Z
# touched on 2025-08-14T20:07:44.141483Z
# touched on 2025-08-14T20:07:58.347905Z
# touched on 2025-08-14T20:08:11.307090Z
# touched on 2025-08-14T20:08:13.542311Z
# touched on 2025-08-14T20:08:17.484215Z
# touched on 2025-08-14T20:08:19.655454Z
# touched on 2025-08-14T20:08:24.157719Z
# touched on 2025-08-14T20:08:30.410949Z
# touched on 2025-08-14T20:08:34.762443Z
# touched on 2025-08-14T20:08:45.294675Z
# touched on 2025-08-14T20:08:47.352134Z
# touched on 2025-08-14T20:08:55.901617Z
# touched on 2025-08-14T20:09:02.155160Z
# touched on 2025-08-14T20:09:08.237533Z
# touched on 2025-08-14T20:09:10.446815Z
# touched on 2025-08-14T20:09:12.486433Z
# touched on 2025-08-14T20:09:14.850168Z
# touched on 2025-08-14T20:09:17.016130Z
# touched on 2025-08-14T20:09:21.195533Z
# touched on 2025-08-14T20:09:30.470800Z
# touched on 2025-08-14T20:09:33.687572Z
# touched on 2025-08-14T20:09:45.810558Z
# touched on 2025-08-14T20:09:51.566821Z
# touched on 2025-08-14T20:09:53.648837Z
# touched on 2025-08-14T20:09:55.763380Z
# touched on 2025-08-14T20:10:04.191012Z
# touched on 2025-08-14T20:10:08.308833Z
# touched on 2025-08-14T20:10:10.430379Z
# touched on 2025-08-14T20:10:16.775575Z
# touched on 2025-08-14T20:10:32.101457Z
# touched on 2025-08-14T20:10:34.177419Z
# touched on 2025-08-14T20:11:03.902976Z
# touched on 2025-08-14T20:11:10.250995Z
# touched on 2025-08-14T20:11:12.401654Z
# touched on 2025-08-14T20:11:14.485827Z
# touched on 2025-08-14T20:11:16.599548Z
# touched on 2025-08-14T20:11:20.696442Z
# touched on 2025-08-14T20:11:24.669974Z
# touched on 2025-08-14T20:11:26.679018Z
# touched on 2025-08-14T20:11:39.438392Z
# touched on 2025-08-14T20:11:46.044154Z
# touched on 2025-08-14T20:11:50.084826Z
# touched on 2025-08-14T20:12:21.782812Z
# touched on 2025-08-14T20:12:23.879478Z
# touched on 2025-08-14T20:12:26.128543Z
# touched on 2025-08-14T20:12:45.182163Z
# touched on 2025-08-14T20:13:08.268386Z
# touched on 2025-08-14T20:13:10.397459Z
# touched on 2025-08-14T20:13:12.517176Z
# touched on 2025-08-14T20:13:14.566124Z
# touched on 2025-08-14T20:13:16.712412Z
# touched on 2025-08-14T20:13:18.694508Z
# touched on 2025-08-14T20:13:24.885885Z