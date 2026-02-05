# Persona → Prospect Finder + Google Sheets Export

A full-stack application that takes a **persona definition** (job title, experience, location, industry, etc.) and returns a **ranked list of matching professional profiles**, with the ability to **export results to Google Sheets and Excel**.  
The system is built with a strong focus on **compliance, security, and clean architecture**.

---

## Features

- Persona-based prospect search
- Apollo-style connector using a seeded dataset (no scraping)
- Match scoring (0–100) with clear explanations
- Profile de-duplication across sources
- PII-safe handling (email/phone only if legally available)
- Export results to **Google Sheets**
- Environment-based configuration
- Modular and extensible backend design

---

## Tech Stack

### Frontend
- React (Vite)
- Axios

### Backend
- Python
- FastAPI
- Pydantic
- Google Sheets API

### Storage
- SQLite (local)

---

## Architecture Overview

Frontend (React + Vite)
|
| REST API
v
Backend (FastAPI)
├── Persona Normalizer
├── Apollo Connector (Seeded Data)
├── Scoring Engine
├── De-duplication
├── Google Sheets Exporter
└── SQLite Storage


---

## Project Structure

persona-prospect-finder/
│
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── routes/prospect.py
│ │ ├── services/
│ │ │ ├── persona_normalizer.py
│ │ │ ├── apollo_connector.py
│ │ │ ├── scorer.py
│ │ │ ├── deduplicator.py
│ │ │ └── sheets_exporter.py
│ │ ├── schemas.py
│ │ └── seed/apollo_seed.json
│ ├── requirements.txt
│ ├── .env (ignored)
│ └── .gitignore
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── main.jsx
│ │ └── components/PersonaForm.jsx
│ ├── index.html
│ ├── package.json
│ └── vite.config.js
│
├── sample-output/
│ ├── prospects.xlsx
│ └── google-sheet-screenshot.png
│
└── README.md


---

## Setup & Run Instructions

### 🔹 Prerequisites

- Python 3.9+
- Node.js 18+
- Git
- Google Cloud account (for Sheets API)

---

### Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
venv\Scripts\activate   
pip install -r requirements.txt
