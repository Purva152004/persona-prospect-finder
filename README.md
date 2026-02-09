# Persona Prospect Finder

Persona Prospect Finder is a full-stack web application that allows users to submit persona or prospect details through a modern frontend UI and automatically store the data in a structured Google Sheet.  
The project also uses seeded dummy data for testing and demonstration.

---
## Features

- Modern, responsive React user interface  
- FastAPI backend with REST APIs  
- Automatic export of data to Google Sheets  
- Structured and formatted sheet output  
- Seeded dummy prospect data for testing  
- Secure Google Sheets integration using Service Account  
- Beginner-friendly project structure  

---
## Tech Stack

### Frontend
- React (Vite)
- JavaScript (ES6+)
- CSS

### Backend
- Python
- FastAPI
- Uvicorn
- Google Sheets API
- python-dotenv

---
## Project Structure

```text
persona-prospect-finder/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   │   └── prospect.py
│   │   ├── services/
│   │   │   ├── sheets_exporter.py
│   │   │   ├── apollo_connector.py
│   │   │   ├── persona_normalizer.py
│   │   │   └── scorer.py
│   │   ├── seed/
│   │   │   └── apollo_seed.json
│   │   ├── schemas.py
│   │   └── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── PersonaForm.jsx
│   │   ├── styles.css
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```
## Prerequisites

- Node.js (v18 or higher)
- Python (v3.10 or higher)
- Git
- Google Cloud account with Google Sheets API enabled

---
## Google Sheets Setup

1. Create a Google Cloud Project  
2. Enable **Google Sheets API**  
3. Create a **Service Account**  
4. Copy the Service Account email  
5. Share your Google Sheet with that email (**Editor access**)  
6. Add credentials in the `.env` file  

## Running Project

### Backend (FastAPI)
```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
### Frontend (React)
```
cd frontend
npm install
npm run dev
```

## Google Sheet Output Format
```
| First Name | Last Name | Title | Company | Location | Industry | Experience | Profile URL | Email | Phone | Score | Source |
|-----------|-----------|-------|---------|----------|----------|------------|-------------|-------|-------|-------|--------|
```

## Use Cases

Full-stack portfolio project
Internship or academic submission
Google Sheets automation
API integration practice
Prospect management demo