# [TITLE OF THE PROJECT] Smart Student Life Optimizer

is a Course Based Project in partial fulfillment of the requirements for the
Course name:  Machine Learning with Python ____________________________
Course code: E1PY210B____________________________
Program: MCA AI/ML______________________________
Semester: 2nd     Section: 8

SUBMITTED BY:
Group member 1 Paras Sharma(25SCSE2240306)
Group member 2 Naman Saini (25SCSE2240307)
Group member 3 Udit Nayan (25SCSE2240308)

SUBMITTED TO:
SCHOOL OF COMPUTER APPLICATIONS & TECHNOLOGY (SCAT)

## DECLARATION 

I/We hereby declare that the project report entitled "Smart Student Life Optimizer" submitted to School of Computer Applications & Technology, Galgotias University in partial fulfillment of the requirement for the award for the degree of ___________________MCA AI/ML___________________, is an authentic and original work carried out by me/us.
The matter embodied in this project is a genuine work done by me / us and has not been submitted whether to this institute or to any other University / Institute for the fulfillment of the requirements of any course of study.
Wherever I/We have used materials (data, mathematical analysis and text) from other sources or have quoted written materials, I/We have given due credit to them by giving their details in the references section.

Name
Enrollment No.
Role
Sign.
Group member 1

Group member 2

(Signature of approving Faculty Member)                                  
Ms./Mr./Dr. ________
____(Emp ID)____
____(Affiliation)____

## ACKNOWLEDGEMENT
First of all, I would like to pay my humble respect to the almighty God for his grace and mercy by which I am able to complete this project.
I would like to express heartiest gratitude to Dr. [Name of Dean], Dean, School of Computer Applications & Technology, Galgotias University for profound and continuous support to work on this project.
Further, I express a deep sense of gratitude to Dr. [Name of Program Chair], Program Chair – BCA/BSC/MCA/MSC, School of Computer Applications & Technology, Galgotias University for their cordial guidance and support to make available all required equipment and the necessary material to complete the project.
I would like to extend my sincerest gratitude to Ms./Mr./Dr. [Name of Faculty Member], [Affiliation/Designation], School of Computer Applications & Technology, Galgotias University for guidance and providing necessary information as well as for the overall support in completing the project.
I acknowledge the suggestion of my parents, peer students, friends and family members and all concerned persons who are associated directly or indirectly in the successful completion of this project.

Date: ________ Signature ________
Name:- ________________
Enrollment No. ________

## Table of Contents
1. Introduction (Preliminary Project Plan)
2. Technical Requirements & Design
3. Technology Readiness: Implementation & Debugging [Code Snippets]
4. Final product: Output screens
5. GitHub Deployment details [Optional]
6. Conclusion & Discussions
7. Bibliography & References
Appendices [if applicable]

---

## [Chapter- 1] Introduction (Preliminary Project Plan)

**Problem statement**
College students often struggle to balance academic performance, personal well-being, and lifestyle habits. Managing attendance, organizing daily schedules, tracking study hours, and maintaining productivity while avoiding distractions can become overwhelming without a centralized, data-driven tool. There is a need for a unified platform that not only tracks these metrics but also leverages Artificial Intelligence to provide actionable insights, predict performance, and optimize daily routines.

**Objective**
- To develop an AI-powered web application that acts as a comprehensive academic productivity and lifestyle dashboard.
- To utilize Machine Learning models to predict student marks, final grades, stress levels, and productivity based on lifestyle and academic data.
- To integrate an OCR-based system for automated attendance tracking from university ERP portal screenshots.
- To provide a dynamic day planner that integrates the student's timetable with real-time predictions to optimize their schedule.

**Proposed Methodology / Workflow**
1. **Data Collection & Preprocessing:** Gather datasets related to student performance, lifestyle, and productivity. Clean and preprocess the data for model training.
2. **Model Training:** Develop and train four Machine Learning models (Linear Regression, Random Forest, Decision Tree) to predict outcomes like marks, grades, stress, and productivity.
3. **Backend Development:** Build a robust Flask-based RESTful backend to serve API endpoints and handle routing.
4. **Frontend Development:** Design an intuitive, responsive, and glassmorphic UI using Bootstrap 5, Jinja2 templates, and Plotly.js for data visualization.
5. **Feature Integration:** Implement the OCR attendance parser using Tesseract and OpenCV, and integrate the dynamic planner module.
6. **Testing & Refinement:** Test the application locally, refine model accuracies, and ensure seamless user experience across the dashboard.

**Expected Outcome**
A fully functional web application running locally on a Flask server that allows students to view their timetables, track their attendance using OCR, log their daily habits, and receive AI-driven predictions regarding their academic performance and stress levels. The dashboard will visually present data analytics to help students make informed decisions about their study routines.

**Future-scope and Limitations**
- **Future Scope:** Integration with external APIs (like Google Calendar), cloud deployment (e.g., AWS or Heroku), mobile application development, and adding a personalized chatbot for study tips.
- **Limitations:** The OCR system heavily depends on the image quality and specific format of the university's ERP portal. The machine learning predictions are based on historical datasets which may not fully capture individual psychological factors. The application currently stores data in local CSV files rather than a scalable relational database.

---

## [Chapter- 2] Technical Requirements & Design

**Libraries, Modules & other dependencies**
- **Web Framework:** Flask (Python)
- **Data Manipulation & Analysis:** pandas, numpy
- **Machine Learning:** scikit-learn, joblib
- **Data Visualization:** plotly
- **Computer Vision & OCR:** opencv-python, pytesseract
- **Frontend Technologies:** HTML5, CSS3, JavaScript, Bootstrap 5, Font Awesome, Inter font

**Software requirements**
- Operating System: Windows 10/11, macOS, or Linux
- Environment: Python 3.8+
- External Tool: Tesseract OCR Engine
- Web Browser: Google Chrome, Mozilla Firefox, or Microsoft Edge

**Hardware requirements**
- Processor: Intel Core i3 / AMD Ryzen 3 or above
- RAM: Minimum 4 GB (8 GB recommended)
- Storage: Minimum 500 MB of free disk space

**Workflow chart / diagram**
1. **User Input:** User uploads timetable, enters study habits, or uploads attendance screenshots via the Web Interface.
2. **Frontend (Jinja2/Bootstrap):** Sends API requests (JSON/Form Data) to the backend.
3. **Flask Backend:**
   - Evaluates API endpoints (e.g., `/api/predict`, `/api/ocr`, `/api/planner`).
   - For Predictions: Loads `.pkl` ML Models -> Processes input -> Returns prediction (Marks, Stress, Productivity).
   - For OCR: Preprocesses image using OpenCV -> Extracts text via Tesseract -> Parses attendance metrics.
4. **Data Handling:** Backend reads/writes to local CSV datasets.
5. **Response:** Processed data is visualized on the Dashboard using Plotly charts or displayed as structured feedback.

**Database schema**
The project utilizes CSV files for data storage and management:
- `timetable.csv`: class schedule (`day`, `time_start`, `time_end`, `subject_code`, `subject_name`, `subject_type`, `section`, `room`, `faculty`).
- `Student_Performance.csv`: Academic records (`study_hours`, `attendance_percentage`, `overall_score`, `final_grade`).
- `student_lifestyle_performance_dataset.csv`: Wellbeing data (`Study_Hours_per_Day`, `Sleep_Hours`, `Screen_Time_Hours`, `Gym_Hours_per_Week`, `Stress_Level_1_to_10`).
- `student_productivity_distraction_dataset_20000.csv`: Daily productivity metrics (`phone_usage_hours`, `social_media_hours`, `breaks_per_day`, `exercise_minutes`, `productivity_score`).

---

## [Chapter- 3] Technology Readiness: Implementation & Debugging

The backend relies on the Flask framework and custom Python routes to integrate data processing and machine learning capabilities. Below is an example code snippet illustrating the `/api/predict` route that aggregates user inputs and loads multiple machine learning models to provide holistic insights.

```python
@app.route('/api/predict', methods=['POST'])
def predict_all():
    if not models_loaded:
        return jsonify({"error": "Models are not loaded on server."}), 500
        
    try:
        data = request.json
        study_hours = float(data.get('study_hours', 4))
        attendance = float(data.get('attendance', 75))
        sleep_hours = float(data.get('sleep_hours', 7))
        screen_time = float(data.get('screen_time', 4))
        gym_hours = float(data.get('gym_hours', 2))
        
        # Load and predict using ML Models
        marks_pred = marks_model.predict(pd.DataFrame([[study_hours, attendance]], columns=['study_hours', 'attendance_percentage']))[0]
        perf_pred_encoded = perf_model.predict(pd.DataFrame([[study_hours, attendance]], columns=['study_hours', 'attendance_percentage']))[0]
        perf_pred = perf_le.inverse_transform([perf_pred_encoded])[0]
        
        stress_features = pd.DataFrame([[study_hours, sleep_hours, screen_time, gym_hours]], columns=['Study_Hours_per_Day', 'Sleep_Hours', 'Screen_Time_Hours', 'Gym_Hours_per_Week'])
        stress_pred = stress_model.predict(stress_features)[0]
        
        return jsonify({
            "marks": round(marks_pred, 2),
            "performance": str(perf_pred).upper(),
            "stress": str(stress_pred)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

---

## [Chapter- 4] Final product: Output screens
*(Please insert screenshots of the Dashboard, Timetable viewer, OCR Attendance upload screen, AI Predictions page, and Analytics charts here)*

---

## [Chapter- 5] GitHub & Deployment details
- **Repository Link:** *(To be added by the user)*
- **Deployment Strategy:** The application is currently designed to be run locally in a Python virtual environment (`venv`). To start the application, the user simply activates the environment and runs `python app.py`, which launches a local Flask development server on `http://127.0.0.1:5000`.

---

## [Chapter- 6] Conclusion & Discussions

The "Smart Student Life Optimizer" successfully achieves its core objective of providing students with an all-in-one platform for managing their academic lives and mental wellbeing. By leveraging Machine Learning and Computer Vision (OCR), the system transcends a traditional digital diary, transforming into an intelligent assistant that provides real-time, data-driven feedback. The project bridges the gap between student lifestyle tracking and academic performance, paving the way for proactive academic counseling. While the current build is optimized for local performance and dependent on ERP screenshot fidelity, it lays a solid foundation for future cloud deployment and broader university integrations.

---

## [Chapter- 7] Bibliography & References
1. Flask Documentation: https://flask.palletsprojects.com/
2. Scikit-Learn Machine Learning Library: https://scikit-learn.org/
3. OpenCV-Python Documentation: https://docs.opencv.org/
4. Tesseract OCR via Pytesseract: https://github.com/madmaze/pytesseract
5. Plotly JS Data Visualization: https://plotly.com/javascript/
6. Bootstrap Frontend Framework: https://getbootstrap.com/

## Appendix
*(Add any additional supplementary materials, extended datasets, or configuration setups here)*
