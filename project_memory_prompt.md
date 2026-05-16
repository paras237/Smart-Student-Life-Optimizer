# 🧠 Project Memory Prompt — Smart Student Life Optimizer

> Copy-paste this entire prompt at the start of any new conversation to give the AI full context about this project.

---

## 📌 Project Overview

**Project Name:** Smart Student Life Optimizer  
**Type:** Flask Web Application (Python backend + HTML/CSS/JS frontend)  
**Purpose:** AI-powered academic productivity and lifestyle dashboard for college students  
**Run Command:**
```powershell
cd "C:\Users\paras\OneDrive\Desktop\Project"
.\venv\Scripts\activate
python app.py
```
**Access URL:** http://127.0.0.1:5000  
**Port:** 5000 (Flask debug mode)

---

## 📁 Project Structure

```
C:\Users\paras\OneDrive\Desktop\Project\
│
├── app.py                          ← Main Flask backend (727 lines)
├── requirements.txt                ← Flask, pandas, numpy, scikit-learn, joblib, plotly, opencv-python, pytesseract
│
├── dataset/
│   ├── timetable.csv               ← User's parsed timetable (day, time_start, time_end, subject_code, subject_name, subject_type, section, room, faculty)
│   └── uploads/                    ← Temporary OCR image uploads
│
├── models/                         ← Pre-trained ML models (joblib .pkl files)
│   ├── marks_predictor.pkl             ← Linear Regression → predicts overall_score
│   ├── performance_classifier.pkl      ← Random Forest → predicts final_grade (A/B/C/D/F)
│   ├── performance_label_encoder.pkl   ← LabelEncoder for above
│   ├── stress_classifier.pkl           ← Random Forest → predicts Stress Level (Low/Moderate/High)
│   └── productivity_classifier.pkl     ← Decision Tree → predicts Productivity (Low/Medium/High)
│
├── ml/
│   └── train_models.py             ← Script to retrain all 4 ML models from scratch
│
├── templates/                      ← Jinja2 HTML pages
│   ├── base.html                   ← Shared layout: sidebar, topbar, Bootstrap 5, Inter font, Plotly, Font Awesome
│   ├── dashboard.html              ← Home/overview page
│   ├── predictions.html            ← AI Predictions page (uses /api/predict)
│   ├── attendance.html             ← OCR Attendance tracker (uses /api/ocr)
│   ├── planner.html                ← Smart Day Planner (uses /api/planner)
│   ├── timetable.html              ← Timetable viewer/uploader (uses /api/timetable/*)
│   ├── analytics.html              ← Charts/graphs (uses /api/analytics_data)
│   └── lifestyle.html              ← Lifestyle & habit tracker
│
├── static/
│   ├── css/style.css               ← Custom CSS (dark theme, glassmorphism)
│   └── js/main.js                  ← Shared JS (sidebar toggle, nav highlight)
│
├── Student_Performance.csv                             ← Dataset 1 (study_hours, attendance_percentage, overall_score, final_grade)
├── student_lifestyle_performance_dataset.csv           ← Dataset 2 (Study_Hours_per_Day, Sleep_Hours, Screen_Time_Hours, Gym_Hours_per_Week, Stress_Level_1_to_10)
└── student_productivity_distraction_dataset_20000.csv  ← Dataset 3 (phone_usage_hours, social_media_hours, breaks_per_day, exercise_minutes, productivity_score)
```

---

## 🌐 All Routes & API Endpoints

### Page Routes
| Route | Template | Description |
|-------|----------|-------------|
| `GET /` | dashboard.html | Main dashboard |
| `GET /predictions` | predictions.html | AI prediction form |
| `GET /attendance` | attendance.html | OCR attendance tracker |
| `GET /planner` | planner.html | Smart day planner |
| `GET /timetable` | timetable.html | Timetable viewer |
| `GET /analytics` | analytics.html | Data analytics charts |
| `GET /lifestyle` | lifestyle.html | Lifestyle habit tracker |

### API Endpoints
| Method | Route | Description |
|--------|-------|-------------|
| `POST` | `/api/predict` | Returns marks, performance grade, stress level, productivity |
| `POST` | `/api/planner` | Generates a dynamic day schedule based on timetable + stress/productivity |
| `GET` | `/api/timetable` | Returns timetable.csv as JSON |
| `GET` | `/api/timetable/download` | Downloads timetable.csv |
| `POST` | `/api/timetable/upload` | Upload a new timetable CSV |
| `POST` | `/api/timetable/parse-text` | Parse tab-separated ERP timetable text into CSV |
| `GET` | `/api/analytics_data` | Returns study_vs_score, stress_dist, prod_trend chart data |
| `POST` | `/api/ocr` | Upload attendance screenshot(s), extract attendance data via Tesseract OCR |

---

## 🤖 ML Models Detail

### 1. Marks Predictor (`marks_predictor.pkl`)
- **Algorithm:** Linear Regression
- **Input features:** `study_hours`, `attendance_percentage`
- **Output:** Predicted `overall_score` (numeric)
- **Dataset:** `Student_Performance.csv`

### 2. Performance Classifier (`performance_classifier.pkl`)
- **Algorithm:** Random Forest (50 trees)
- **Input features:** `study_hours`, `attendance_percentage`
- **Output:** Grade label (A/B/C/D/F) via `performance_label_encoder.pkl`
- **Dataset:** `Student_Performance.csv`

### 3. Stress Classifier (`stress_classifier.pkl`)
- **Algorithm:** Random Forest (50 trees)
- **Input features:** `Study_Hours_per_Day`, `Sleep_Hours`, `Screen_Time_Hours`, `Gym_Hours_per_Week`
- **Output:** `"Low Stress"` / `"Moderate Stress"` / `"High Stress"`
- **Dataset:** `student_lifestyle_performance_dataset.csv`

### 4. Productivity Classifier (`productivity_classifier.pkl`)
- **Algorithm:** Decision Tree (max_depth=5)
- **Input features:** `phone_usage_hours`, `social_media_hours`, `breaks_per_day`, `exercise_minutes`
- **Output:** `"Low Productivity"` / `"Medium Productivity"` / `"High Productivity"`
- **Dataset:** `student_productivity_distraction_dataset_20000.csv`

> **To retrain models:** `python ml/train_models.py` (run from project root)

---

## 📅 Timetable System

- Stored at `dataset/timetable.csv`
- **Required columns:** `day`, `time_start`, `time_end`, `subject_code`, `subject_type`
- **Optional columns:** `subject_name`, `section`, `room`, `faculty`
- **Subject types:** `PP` = Lecture, `PR` = Lab/Practical

### Subject Code Mapping (hardcoded in app.py)
| Subject Name | Code |
|---|---|
| Data Structures | E1PY203B |
| Artificial Intelligence Generative AI | E1PY213T |
| Machine Learning with Python | E1PY210B |
| Object Oriented Programming with Java | E1PY201B |
| Internet of Things | E1PY217T |
| Verbal and Quantitative Reasoning | 01PA202L |
| Operating Systems | E1PY207T |
| Data Communication and Networking | E1PY206T |
| Training-I | E1PY218L |

---

## 🔍 OCR Attendance System

- Uses **OpenCV** for image preprocessing + **Tesseract OCR** for text extraction
- Supports **multiple screenshot uploads** (stitched vertically)
- Parses the university ERP "Attendance Details" screen format
- **Tesseract path auto-detection** (checks Program Files, Program Files (x86), LOCALAPPDATA)
- Fallback: Shows hardcoded real attendance data if Tesseract is not installed
- **OCR notes returned:** `OCR_SUCCESS`, `OCR_SUCCESS_WITH_TOTAL`, `TIMETABLE_DETECTED`, `DEMO_REAL_DATA`

---

## 🎨 UI / Design System

- **Framework:** Bootstrap 5.3.2
- **Font:** Inter (Google Fonts) — weights 300–800
- **Icons:** Font Awesome 6.4.0
- **Charts:** Plotly.js (latest CDN)
- **Theme:** Dark mode with glassmorphism effects
- **Layout:** Fixed sidebar + scrollable content area (sidebar toggle via `#menu-toggle`)
- **CSS:** `static/css/style.css`
- **JS:** `static/js/main.js` (sidebar toggle + active nav link highlighting)

---

## 📦 Dependencies (`requirements.txt`)
```
Flask
pandas
numpy
scikit-learn
joblib
plotly
opencv-python
pytesseract
```

---

## ⚙️ Key Configuration

- `app.config['SECRET_KEY']` = `'smart-student-optimizer-secret'`
- Models loaded at startup from `models/` directory; `models_loaded = False` if any fail
- Auto-creates folders on startup: `models/`, `dataset/`, `static/css`, `static/js`, `templates/`, `dataset/uploads/`
- Virtual environment located at `.\venv\`

---

## 🚀 Quick Commands

```powershell
# Run the app
cd "C:\Users\paras\OneDrive\Desktop\Project"
.\venv\Scripts\activate
python app.py

# Retrain ML models
python ml/train_models.py

# Install dependencies (if venv is fresh)
pip install -r requirements.txt
```
